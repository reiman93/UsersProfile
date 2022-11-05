from dataclasses import field, fields
from rest_framework import serializers

from api_profile_crud.models import Profile,Interaction

class ProfileSerializers(serializers.ModelSerializer):
    #img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model   = Profile
        fields  = ['id','first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode', 'available']

class InteractionSerializers(serializers.ModelSerializer):
    class Meta:
        model   = Interaction
        fields  = ['id','profile_left', 'profile_right']
