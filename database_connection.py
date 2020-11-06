"""""
database_connection.py is to make the connection to the database and gets the template and the variable details
"""""

from pymongo import MongoClient
from env_var import Database, Cluster, Collection


# Connects to the database and returns the collection
def get_collection():
    cluster = MongoClient(Database)
    db = cluster[Cluster]
    collection = db[Collection]
    return collection


# returns the variables of the template with the given id
def get_template_variables(id):
    collection = get_collection()
    template = list(collection.find({'_id': int(id)}))
    try:
        variables = template[0]['variables']['variable']
    except:
        variables = None
    return variables


# returns the list of all templates
def get_templates():
    collection = get_collection()
    templates = list(collection.find())
    return templates


# returns the template with the given id
def get_template(id):
    collection = get_collection()
    template = list(collection.find({'_id': int(id)}))
    return template[0]

