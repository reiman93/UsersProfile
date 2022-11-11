import os
import time
import django.random as rd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "users_profile.settings")

django.setup()

from api_profile_crud.models import Profile, Interaction

vocals=["a","e","i","o","u"]
consonats=["b", "c", "d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

