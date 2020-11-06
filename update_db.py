"""""
update_db.py is to update the Database with the templates from the Prime Infrastructure
"""""

from database_connection import get_collection
from datetime import datetime

import requests
import urllib3

from requests.auth import HTTPBasicAuth

from env_var import PI1


def insert_templates(prime):
    # gets the collection in tha database
    collection = get_collection()

    # API call to get the cli templates
    url = 'https://{0}/webacs/api/v3/data/CliTemplate.json'.format(prime['base_url'])
    basicAuth = HTTPBasicAuth(prime['username'], prime['password'])
    querystring = {".full": "true"}
    ssl_verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url, params=querystring, auth=basicAuth, verify=ssl_verify)
    parsed_response = response.json()

    for entity in parsed_response["queryResponse"]['entity']:
        name = entity["cliTemplateDTO"]["name"]
        id = entity["cliTemplateDTO"]["templateId"]
        author = entity["cliTemplateDTO"]["author"]
        create_date = entity["cliTemplateDTO"]["createdOn"]
        content = entity["cliTemplateDTO"]["content"]
        try:
            description = entity["cliTemplateDTO"]["description"]
        except:
            description = ''
        try:
            deviceType = entity["cliTemplateDTO"]["deviceType"]
        except:
            deviceType = ''
        try:
            tags = entity["cliTemplateDTO"]["tags"]
        except:
            tags = ''
        try:
            variables = entity["cliTemplateDTO"]["variables"]
        except:
            variables = ''
        try:
            version = entity["cliTemplateDTO"]["version"]
        except:
            version = ''
        date = datetime.now()
        today = date.strftime('%H:%M %m-%d-%Y')

        # insert the parsed response into the database
        collection.insert_one(
            {"_id": id, "id": id, "name": name, "description": description, "create_date": create_date,
             "author": author, "version": version,
             "content": content, "deviceType": deviceType, "tags": tags, "variables": variables, 'update_date': today})

    print('The database has been updated with the templates from the Prime Environment')


# add the prime instance you would like to get the templates from
insert_templates(PI1)
