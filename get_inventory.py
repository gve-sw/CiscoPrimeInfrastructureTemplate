"""""
get_inventory.py is to get a list of all the devices in the selected PI
"""""
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from env_var import prime_list

def get_prime(id):
    for pi in prime_list:
        if pi['id'] == id:
            return pi

# Returns list of all devices in the Prime Infrastructure with the selected id by making the API call
def inventory(id):
    # selects the prime infrastructure
    prime_instance = get_prime(int(id))

    # api call to get all the devices
    url = 'https://{0}/webacs/api/v4/data/Devices.json'.format(prime_instance['base_url'])
    basicAuth = HTTPBasicAuth(prime_instance['username'], prime_instance['password'])
    querystring = {".full": "true"}
    ssl_verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url, params=querystring, auth=basicAuth, verify=ssl_verify)
    parsed_response = response.json()
    devices = []
    print(parsed_response["queryResponse"]['entity'])
    # parse the api response
    for entity in parsed_response["queryResponse"]['entity']:
        ip = entity["devicesDTO"]["ipAddress"]
        try:
            name = entity["devicesDTO"]["deviceName"]
        except:
            name = ''
        try:
            id = entity["devicesDTO"]["@id"]
        except:
            id = ''
        # add all the devices to the list

        devices.append({"name": name, "id": id, "ip": ip})
    return devices