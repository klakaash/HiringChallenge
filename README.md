# HiringChallenge

This project is used to extract the medicine information from a sentence.

## About the Project

The project is built using Django with the medicine data posted in the DB. We first extract the medicine name using spacy library and then find the matching 
medicine name and then its details from the DB.

## Endpoint Used

The project uses 2 endpoints:

1. /create [POST]-> This endpoint should be called first as this populates the DB with the CSV data given which will help us query the medicine information later.
2. /get_entity [POST]-> This endpoint takes in a json body in the request and returns the corresponding medicine information.

### Usage:
/create -> Making a POST request to the localhost 8000 port will add all the information to the DB. Returns a 201 status.

/get_entity -> Making a POST request to the localhost 8000 port with a json body of key sentence which holds the user's input will allows us to extract the medical information
              JSON Body:
              
```
{"sentence": "Want to buy a Oloworm"}
```

## How to run the project

1. Clone this repo and move into the project folder
2. Create a virtual environment to use for all the installations of packages.
3. Install all the requirements using the command ``` pip install -r medicine/requriements.txt ```
4. Now use the command ``` python manage.py makemigrations ``` and ``` python manage.py migrate ``` to use the table.
5. Now run the django server using the command ``` python manage.py runserver ``` .
6. First make an request to the endpoint ``` /create ``` as this will populate the DB
7. Now start using the ``` /get_entity ``` and start querying for medicine names.
  

