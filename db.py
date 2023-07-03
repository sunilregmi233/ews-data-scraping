from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

db_url = config('DB_URL', cast = str)
db_name = config('DB_NAME', cast = str)
db_collection = config('DB_NAME', cast = str)

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