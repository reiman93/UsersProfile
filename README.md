# UsersProfile
This repository contains a CRUD + List of user profiles and models the relationship between them with graph behavior.

nstructions to start the project:
Initial requirements:
 -Have python >= 3.9.5 installed
 -Have Django = 4.0.5 installed

1- Install the necessary dependencies for the project to work correctly, these are:

1.1. rest_framework: used to generate the API

 pip install djangorestframework

1.2 rest_framework_swagger and drf_yasg: to generate the api documentation

 pip install django-rest-swagger
 pip install drf-yasg

1.3 django_seed to generate seeds that initially populate the database.
pip install django-seed

1.4 networkx to model the friendship between users as a graph
pip install networkx
You can also install them all at once by running the command:
pip install -R dependence.txt

The dependency.txt file contains the names of all the dependencies mentioned above.

2- execute the commands:
py manage.py makemigrations
py manage.py migrate
py manage.py runserver

The database file is clean, however, if you want to make sure you can call the service
profile/clean with a get request.

If you want to initially populate the database via a fake data load, stop the django server
and run the following script:
start.py and follow the instructions.
If your terminal or IDE doesn't recognize the script try running it as follows:
./start.py.

then run py manage.py runserver again.

You can now test all the services in users_profile.
