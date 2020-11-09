# Cisco Prime Infrastructure Configuration Template Automation
Store Configuration Templates in local database to have a centralized configuration base for all your templates, create new templates and deploy templates on servers. 

## Contacts
* Eda Akturk (eakturk@cisco.com)

## Solution Components
*  Cisco Prime Infrastructure (https://developer.cisco.com/site/prime-infrastructure/)
*  MongoDB (https://www.mongodb.com/)
*  Python 3.8 (https://www.python.org/)

## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

Now you have your virtual environment setup and ready

#### Install the libraries :

```$ pip install -r requirements.txt```


## Setup: 
*PI Connection*
1. Add the PI details in env_var.py file.
```
PI1 = {
    "id": ,
    "base_url": '',
    "username": '',
    "password": '',
    "hostName": '',
}
PI2 = {
    "id": ,
    "base_url": '',
    "username": '',
    "password": '',
    "hostName": '',
}
```
*Database Connection*

2. Download and Install MongoDB from https://www.mongodb.com/. 

3. Create a collection in MongoDB and add the credentials to env_var.py.  
```
    Database = ''
    Cluster = ''
    Collection = ''
```

*Update Database*

4. Select the PI you would like the local database with and add it into update_db.py   
```
    insert_templates("PI1")
```

5. Run the command to update the Database.   
```
    $ python update_db.py 
```

Now you have completed the setup and updated the database, you are now ready to run the web application. 

## Usage: 
Run the python script
```
    $ python start.py
```

From the Flask application you can:
*  View all the templates in you local database
*  View all the inventory on the selected PI instance
*  Create a new template for the selected PI instance 
*  Deploy a job to a device in the selected PI instance

# Screenshots
Here are some sample screenshots of the prototype.

*Choose Prime Instance:*
![/IMAGES/prime_instance.PNG](/IMAGES/prime_instance.PNG)

*Select Template from local database to add to selected PI:*
![/IMAGES/create.PNG](/IMAGES/create.PNG)

*Select template and select device to create job to deploy template:*
![/IMAGES/deploy.PNG](/IMAGES/deploy.PNG)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.

![/IMAGES/0image.png](/IMAGES/0image.png)
