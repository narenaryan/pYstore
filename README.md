pYstore
=======

Python application for storing functions and objects in Mongo db and retreiving them later.
The frequently used procedures can be stored in a database as a record.SQL databases uses dead hard mappers to perform the task,but NoSQL databases like MongoDB,CouchDB are BSON,JSON structured which facilitates to store objects as documents.

Common steps:
1.Create a user defined object with all the functions to be stored as its memebers.
2.MongoDB stores documents in BSON format.So we should convert object to BSON before storing it in MongoDB.
3.binary encoders and decoders are used for converting object to binary.
4.SONManipulator object in MongoDB is used to auto encode and decode dictionary to BSON strings.


Note:
this application uses test data object,modification is required according to the context of use.
