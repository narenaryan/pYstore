__author__ = 'naren'
from bson.binary import Binary
from pymongo.son_manipulator import SONManipulator
import pymongo
from data import *
#connecting to mongodb
conn=pymongo.Connection(host="localhost",port=27017)
#fetching database handle for proc(procedures) table
db=conn['proc']
db.proc.remove()
def to_binary(custom):
    '''CONVERTS USER DEFINED OBJECT TO BINARY IN ORDER TO STORE IN DATABASE'''
    return Binary(str(custom.getx()), 128)

def from_binary(binary):
    '''CONVERTS DATABASE STORED OBJECT TO USER DEFINED OBJECT'''
    return UserDefined(int(binary))


class TransformToBinary(SONManipulator):
    '''THIS CLASS AUTOMATICALLY ENCODE AND DECODE DATA INTO AND FROM BSON FORMAT'''
    def transform_incoming(self, son, collection):
     for (key, value) in son.items():
       if isinstance(value,UserDefined):
         son[key] = to_binary(value)
       elif isinstance(value, dict):
         son[key] = self.transform_incoming(value, collection)
     return son
    def transform_outgoing(self, son, collection):
         for (key, value) in son.items():
           if isinstance(value, Binary) and value.subtype == 128:
             son[key] = from_binary(value)
           elif isinstance(value, dict):
             son[key] = self.transform_outgoing(value, collection)
         return son
db.add_son_manipulator(TransformToBinary())
#inserting object and so its functions in the mongo document
db.proc.insert({"usrdefind":UserDefined(31)})
#retriving object from db and applying function on it
print (db.proc.findOne()["usrdefind"]).getx()

