from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from api_profile_crud.models import Profile, Interaction

class GraphTestCase(TestCase):
    def test_get_frens(self):
    
        client = APIClient()
        
        prof1=Profile.objects.create(
            first_name="Ned",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        prof2=Profile.objects.create(
            first_name="Robert",
            last_name="Baratheon",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        prof3=Profile.objects.create(
            first_name="Theon",
            last_name="Grenjoy",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof4=Profile.objects.create(
            first_name="Cersi",
            last_name="Lannister",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
       
        prof5=Profile.objects.create(
            first_name="The dog",
            last_name="Clegane",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
       
        Interaction.objects.create(
            profile_left = prof2,
		    profile_right= prof1           
        )
        
        Interaction.objects.create(
            profile_left = prof2,
		    profile_right= prof5           
        )
       
        Interaction.objects.create(
            profile_left = prof3,
		    profile_right= prof2            
        )
        
        Interaction.objects.create(
            profile_left = prof4,
		    profile_right= prof1            
        )

        response = client.get('/profile/frens/{0}/'.format(prof2.id) )
        result = json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 3)

    def test_get_frens_not_found_user(self):
        
        client = APIClient()
        
        prof1=Profile.objects.create(
            first_name="Ned",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        prof2=Profile.objects.create(
            first_name="Robert",
            last_name="Baratheon",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        prof3=Profile.objects.create(
            first_name="Theon",
            last_name="Grenjoy",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof4=Profile.objects.create(
            first_name="Cersi",
            last_name="Lannister",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
       
        prof5=Profile.objects.create(
            first_name="The dog",
            last_name="Clegane",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
       
        Interaction.objects.create(
            profile_left = prof2,
		    profile_right= prof1           
        )
        
        Interaction.objects.create(
            profile_left = prof2,
		    profile_right= prof5           
        )
       
        Interaction.objects.create(
            profile_left = prof3,
		    profile_right= prof2            
        )
        
        Interaction.objects.create(
            profile_left = prof4,
		    profile_right= prof1            
        )

        response = client.get('/profile/frens/{0}/'.format(444) )
        result = json.loads(response.content)

        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
