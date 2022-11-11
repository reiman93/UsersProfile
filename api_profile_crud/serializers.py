from dataclasses import field, fields
from rest_framework import serializers

from api_profile_crud.models import Profile,Interaction

class ProfileSerializers(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, allow_null=True, required=False)
    class Meta:
        model   = Profile
        fields  = ['id','img','first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode', 'available']

class InteractionSerializers(serializers.ModelSerializer):
    class Meta:
        model   = Interaction
        fields  = ['id','profile_left', 'profile_right']
