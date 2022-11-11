from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from api_profile_crud.models import Profile

class CleanTestCase(TestCase):
    
    def test_clean(self):
    
        client = APIClient()
        
        prof=Profile.objects.create(
            first_name="Jhon Snow",
            last_name="Walters",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        response = client.delete(
            '/profile/clean', 
            format='json'
        )
         
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

