import pymongo
from urllib.parse import quote_plus


def upload_to_cloud(data:dict, db_name="IITB", collection_name="weather"):
    # URL-encode the username and password
    username = quote_plus("chandankr014")
    encoded_password = quote_plus("qwerty@1234")
    try:
        client =  pymongo.MongoClient(
            f"mongodb+srv://{username}:{encoded_password}@cluster0.cfw5xma.mongodb.net/?retryWrites=true&w=majority"
        )
        db = client[db_name] #IITB
        collection = db[collection_name] #weather

        collection.insert_one(data)
        print(f"Uploaded to {db_name}.{collection_name} collection in MongoDB")

    except Exception as e:
        print(f"An error occurred: {e}")