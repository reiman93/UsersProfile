from django_seed import Seed
from api_profile_crud.models import Profile, Interaction

print("Type the number of profiles to generate for the initial load")
cant_of_profiles=input()

print("Type the number of connections to generate for the initial load")
cant_of_conections=input()

top=(cant_of_profiles*(cant_of_profiles-1))/2

if  cant_of_conections >= top:
    while cant_of_conections >= top: 
        print("For the number of profiles entered, it is only possible to generate a number of {0} correct connections".format(top))
        print("Enter a new amount")
        cant_of_conections=input()

seeder = Seed.seeder()

seeder.add_entity(Profile, cant_of_profiles)
seeder.add_entity(Interaction, cant_of_conections)

inserted = seeder.execute()

print("                   Datos generados                            ")
print("**************************************************************")