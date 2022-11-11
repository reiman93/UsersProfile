import os
print("Teclee la cantidad de perfiles a generar para la carga inicial")
cant_of_profiles=input()

print("Teclee la cantidad de conexiones a generar para la carga inicial")
cant_of_conections=input()

os.system('python manage.py seed api_profile_crud --number={0}'.format(cant_of_profiles))

