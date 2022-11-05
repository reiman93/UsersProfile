from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from api_profile_crud.models import Profile

class ProfileTestCase(TestCase):

    
    def test_create_profile(self):

        client = APIClient()
       # client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        test_profile = {
            "first_name": "Steph",
            "last_name": "Walters",
            "phone": "(820) 289-1818",
            "address": "5190 Center Court Drive",
            "city": "Spring",
            "state": "TX",
            "zipcode": "77370",
            "available": "true"
        }

        response = client.post(
            '/profile/profile', 
            test_profile,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('first_name', result)
        self.assertIn('last_name', result)
        self.assertIn('phone', result)
        self.assertIn('address', result)
        self.assertIn('city', result)
        self.assertIn('state', result)
        self.assertIn('zipcode', result)
        self.assertIn('available', result)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    
    def test_update_profile(self):

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

        test_profile = {
            "first_name":"Steph",
            "last_name":"Walters",
            "phone":"(820) 289-1818",
            "address":"5190 Center Court Drive",
            "city":"Spring",
            "state":"TX",
            "zipcode": 77370,
            "available":True
        }

        response = client.put(
            '/profile/profile/{0}/'.format(prof.id), 
            test_profile,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_profile)

    
    def test_delete_profile(self):

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
        print("********************************************************")
        print(prof.id)
        print("********************************************************")
        print("service")
        
        response = client.delete(
            '/profile/profile/{0}/'.format(prof.id), 
            format='json'
        )
        print("****************************url**************")
        print(response)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        profile_exists = Profile.objects.filter(id=prof.id)
        self.assertFalse(profile_exists)


    def test_get_profile(self):

        client = APIClient()
        
        Profile.objects.create(
            first_name="Steph",
            last_name="Walters",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        Profile.objects.create(
            first_name="Aria",
            last_name="Walters",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        Profile.objects.create(
            first_name="Sansa",
            last_name="Walters",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        Profile.objects.create(
            first_name="Jhon Snow",
            last_name="Walters",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        response = client.get('/profile/profile')

        result = json.loads(response.content)

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(result), 4)