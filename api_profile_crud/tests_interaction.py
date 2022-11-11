from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from api_profile_crud.models import Profile, Interaction

class InteractionTestCase(TestCase):

    def test_create_interaction_profile_not_found(self):
        
        client = APIClient()
        
        prof1=Profile.objects.create(
            first_name="Sansa",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof2=Profile.objects.create(
            first_name="Jhon Snow",
            last_name="Targarian",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        Interaction.objects.create(
            profile_left = prof1,
		    profile_right= prof2            
        )    
        
        test_interaction = 	{
		"profile_left": 1000,
		"profile_right": prof2.id
	    }

        response = client.post(
            '/profile/interaction', 
            test_interaction,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_interaction_duplicate_edge(self):
    
        client = APIClient()
        
        prof1=Profile.objects.create(
            first_name="Sansa",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof2=Profile.objects.create(
            first_name="Jhon Snow",
            last_name="Targarian",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        Interaction.objects.create(
            profile_left = prof1,
		    profile_right= prof2            
        )    
        
        test_interaction = 	{
		"profile_left": prof1.id,
		"profile_right": prof2.id
	    }

        response = client.post(
            '/profile/interaction', 
            test_interaction,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_interaction_loop(self):
        
        client = APIClient()
        
        prof1=Profile.objects.create(
            first_name="Sansa",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof2=Profile.objects.create(
            first_name="Jhon Snow",
            last_name="Targarian",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        test_interaction = 	{
		"profile_left": prof1.id,
		"profile_right": prof2.id
	    }

        response = client.post(
            '/profile/interaction', 
            test_interaction,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   
    def test_create_interaction(self):

        client = APIClient()
        
        prof1=Profile.objects.create(
            first_name="Sansa",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof2=Profile.objects.create(
            first_name="Jhon Snow",
            last_name="Targarian",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        test_interaction = 	{
		"profile_left": prof1.id,
		"profile_right": prof2.id
	    }

        response = client.post(
            '/profile/interaction', 
            test_interaction,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('profile_left', result)
        self.assertIn('profile_right', result)

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    
    def test_update_interaction(self):

        client = APIClient()

        prof1=Profile.objects.create(
            first_name="Sansa",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof2=Profile.objects.create(
            first_name="Jhon Snow",
            last_name="Targarian",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        prof3=Profile.objects.create(
            first_name="Area",
            last_name="Stark",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )        
        
        inter=Interaction.objects.create(
            profile_left = prof1,
		    profile_right= prof2           
        )
        
        test_interaction = 	{
		"profile_left": prof1.id,
		"profile_right": prof2.id
	    }
        
        response = client.put(
            '/profile/interaction/{0}/'.format(inter.id), 
            test_interaction,
            format='json'
        )
        
        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_interaction)

    
    def test_delete_interaction(self):

        client = APIClient()
        
        prof1=Profile.objects.create(
            first_name="Jorfree",
            last_name="Baratheon",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )
        
        prof2=Profile.objects.create(
            first_name="Holena",
            last_name="Tyrell",
            phone="(820) 289-1818",
            address="5190 Center Court Drive",
            city="Spring",
            state="TX",
            zipcode="77370",
            available=True
        )

        inter=Interaction.objects.create(
            profile_left = prof1,
		    profile_right= prof2            
        )    
            
        response = client.delete(
            '/profile/interaction/{0}/'.format(inter.id), 
            format='json'
        )
  

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        interaction_exists = Interaction.objects.filter(id=inter.id)
        self.assertFalse(interaction_exists)

    def test_get_interaction(self):

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
       
        Interaction.objects.create(
            profile_left = prof2,
		    profile_right= prof1           
        )
       
        Interaction.objects.create(
            profile_left = prof3,
		    profile_right= prof4            
        )
        
        Interaction.objects.create(
            profile_left = prof4,
		    profile_right= prof1
        )

        response = client.get('/profile/interaction')

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(result), 3)
