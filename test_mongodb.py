from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_DB_URL")

if not uri:
    raise ValueError("MONGO_DB_URL is not set in environment variables")

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ Connection failed:", e)