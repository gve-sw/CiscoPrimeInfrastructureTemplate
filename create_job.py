"""""
deploy_template: is to apply the configuration template to the server
add_template: is to create a new template in the PI with a given template-id in the database 
"""""
import requests
import urllib3
from flask import json
from requests.auth import HTTPBasicAuth

from get_inventory import get_prime
from database_connection import get_template_variables, get_template

def deploy_template(id, servers, template_id, template_name):
    prime_instance = get_prime(int(id))

    basicAuth = HTTPBasicAuth(prime_instance['username'], prime_instance['password'])
    headers = {'Content-Type': 'application/json'}
    querystring = {".full": "true"}
    ssl_verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = 'https://{0}/webacs/api/v4/op/cliTemplateConfiguration/deployTemplateThroughJob.json'.format(prime_instance['base_url'])

    variable_data = get_template_variables(template_id)

    if variable_data is '':
        data = {
            "cliTemplateCommand": {
                "targetDevices": {
                    "targetDevice": {
                        "targetDeviceID": servers,
                    }
                },
                "templateName": template_name
            }
        }
    else:
        data = {
            "cliTemplateCommand": {
                "targetDevices": {
                    "targetDevice": {
                        "targetDeviceID": servers,
                        "variableValues": {
                            "variableValue": variable_data
                        }
                    }
                },
                "templateName": template_name
            }
        }

    response = requests.put(url, params=querystring, auth=basicAuth, verify=ssl_verify, headers=headers,data=json.dumps(data))
    return response.json()


def add_template(id, template_id):

    prime = get_prime(int(id))
    template = get_template(template_id)

    template_data = {
        "cliTemplate": {
            "content": template['content'],
            "description": template['description'],
            "deviceType": template['deviceType'],
            "name": 'TEST-' + template['name'],
            # "path" : ,
            "tags": template['tags'],
            "variables": template['variables'],
            "version": template['version'],
        }
    }

    # API call to create template
    url = 'https://{0}/webacs/api/v4/op/cliTemplateConfiguration/upload.json'.format(prime['base_url'])
    basicAuth = HTTPBasicAuth(prime['username'], prime['password'])
    querystring = {".full": "true"}
    ssl_verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, auth=basicAuth, headers=headers, verify=ssl_verify, data=json.dumps(template_data), params=querystring)

    return response.json()