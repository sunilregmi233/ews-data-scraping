from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config
import json

db_url = config('DB_URL', cast = str)
# db_name = config('DB_NAME', cast = str)
# db_collection = config('DB_COLLECTION', cast = str)
# print(db_collection)

def db_conn():
    uri = db_url
    # Create a new client and connect to the server
    client = AsyncIOMotorClient(uri)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return  client

# uri = db_url
# # Create a new client and connect to the server
# client = AsyncIOMotorClient(uri)
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# #     return  client


# db_flood = client.db_name
# db_waterlvl = db_flood.db_collection

# document = {
#             'Basin       '  : 'qwerqwer',
#             'Station-name'  : 'asdfg',
#             'Date        '  : '2021-2-3',
#             'Time        '  : '30:00',
#             'Water- level'  : '3.25m',
#             'Status      '  : 'Below warning level',
#         }
# # document = json.dumps(document, indent = 4) 

# async def do_insert(document):
#     # document = {'key': 'value'}
#     result = await client["flood"]["waterlvl"].insert_one(document)
#     print('result %s' % repr(result.inserted_id))


# import asyncio
# loop = client.get_io_loop()
# loop.run_until_complete(do_insert(document))
# # db_waterlvl.insert_one(document)
# client.close()