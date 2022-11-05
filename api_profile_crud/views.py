from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializers, InteractionSerializers
from .models import Profile, Interaction
from rest_framework import status
from django.http import Http404, JsonResponse, HttpResponse
from django.core import serializers


class Profile_APIView(APIView):   
    def get(self, request, format=None, *args, **kwargs):
        profile = Profile.objects.all()
        serializer = ProfileSerializers(profile, many=True)
        
        return Response(serializer.data)    
    
    def post(self, request, format=None):
        serializer = ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class Profile_APIView_Detail(APIView):    
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404    
    
    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile)  
        return Response(serializer.data)    
    
    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
       
    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Profile_Interactions_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        interaction = Interaction.objects.all()
        serializer = InteractionSerializers(interaction, many=True)
        
        return Response(serializer.data)    
    
    def post(self, request, format=None):
        serializer = InteractionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class Profile_Interactions_APIView_Detail(APIView):    
    def get_object(self, pk):
        try:
            return Interaction.objects.get(pk=pk)
        except Interaction.DoesNotExist:
            raise Http404    
    
    def get(self, request, pk, format=None):
        interaction = self.get_object(pk)
        serializer = InteractionSerializers(interaction)  
        return Response(serializer.data)    
    
    def put(self, request, pk, format=None):
        interaction = self.get_object(pk)
        serializer = InteractionSerializers(interaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
       
    def delete(self, request, pk, format=None):
        interaction = self.get_object(pk)
        interaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Graph_APIView(APIView):
        def get(self, request, pk, format=None):
            interactions = Interaction.objects.all()
            frens=[]
            for i in interactions:
                if  i.profile_right.id==pk:
                    frens.append(i.profile_left)   
                if  i.profile_left.id==pk:
                    frens.append(i.profile_right)    
            print(len(frens))  
            
            frens=serializers.serialize("json",frens)   
            return HttpResponse(frens,content_type="json-comment-filtered")
        
        def post(self, request, format=None):
            source=request.data["source"]
            tarjet=request.data["tarjet"]
            interactions = Interaction.objects.all()
            vertices=[]
            distances=[]
            
            for i in interactions:
                if  i.profile_right.id==source and i.profile_right.id not in vertices:
                    vertices.append(i.profile_left.id)   
                if  i.profile_left.id==source and i.profile_left.idnot not in vertices:
                    vertices.append(i.profile_right.id)  
            c=0
            for j in vertices:
                for k in interactions:
                    if  k.profile_right.id==j and k.profile_right.id not in vertices:
                        vertices.append(i.profile_left.id)   
                    if  i.profile_left.id==source and i.profile_left.idnot not in vertices:
                        vertices.append(i.profile_right.id)  
                
                
            
            
                
                
            

    
        