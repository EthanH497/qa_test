import json
from bson import json_util
from .mongo_client import users_collection


def find_all_users():
    # Find all documents in user db
    cursor = users_collection.find()

    # Extract all objects from cursor
    documents = []
    for document in cursor:
        documents.append(document)

    # Return documents
    return json.loads(json_util.dumps(documents))


def insert_one_user(client_code: str, organization: str):
    # Insert one user with provided client_code and organization
    result = users_collection.insert_one({"client_code": client_code, "organization": organization})

    # Return object id of inserted user document
    return json.loads(json_util.dumps(result.inserted_id))


def update_one_user(client_code: str, new_code: str):
    # Filter user by client_code
    filter = {'client_code': client_code}

    # New client code value
    new_value = {"$set": {'client_code': new_code}}

    # Update document
    result = users_collection.update_one(filter, new_value)

    # Return modified document count
    return json.loads(json_util.dumps(result.modified_count))


def delete_one_user(client_code: str, organization: str):
    # Delete user by client_code and organization
    result = users_collection.delete_one({"client_code": client_code, "organization": organization})

    # Return deleted document count
    return json.loads(json_util.dumps(result.deleted_count))
