from django.http import Http404
from django.urls import re_path
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='api') 
urlpatterns = [ re_path(r'^$', schema_view) ] 

import networkx as nx

from .models import Interaction, Profile
from .serializers import InteractionSerializers, ProfileSerializers


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
        profile_left=request.data["profile_left"]
        profile_right=request.data["profile_right"]
        
        profile_validate_left=[]
        profile_validate_right=[]
        
        profile_validate_left=Profile.objects.filter(id=profile_left)
        profile_validate_right=Profile.objects.filter(id=profile_right)
        
        if profile_left==profile_right:
            return Response("a recursive profile connection cannot be established. You must enter different ids.", status=status.HTTP_400_BAD_REQUEST)
        
        if len(profile_validate_left)==0 or len(profile_validate_right)==0:
            return Response("some of the provided profiles do not exist.", status=status.HTTP_404_NOT_FOUND)
                    
        interactions_vaidate=Interaction.objects.filter(profile_left=profile_left,profile_right=profile_right)
        interactions_vaidate_riverse=Interaction.objects.filter(profile_left=profile_right,profile_right=profile_left)
        
        if len(interactions_vaidate)>0 or len(interactions_vaidate_riverse)>0:
            return Response("These profiles are already friends. Provide another combination.", status=status.HTTP_400_BAD_REQUEST)
        
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
            profile=Profile.objects.filter(id=pk)
            if len(profile)==0:
                return Response("the provided profile do not exist.", status=status.HTTP_404_NOT_FOUND)
                
            interactions = Interaction.objects.all()
            frens=[]
            for i in interactions:
                if  i.profile_right.id==pk:
                    frens.append(i.profile_left.id)   
                if  i.profile_left.id==pk:
                    frens.append(i.profile_right.id)    
            
            frens= Profile.objects.filter(id__in=frens)
            serializer = ProfileSerializers(frens, many=True)
        
            return Response(serializer.data)    

        
class Graph_edge_APIView(APIView):
    def post(self, request, format=None):
        profile_left=request.data["source"]
        profile_right=request.data["tarjet"]
        
        profile_validate_left=[]
        profile_validate_right=[]
        
        profile_validate_left=Profile.objects.filter(id=profile_left)
        profile_validate_right=Profile.objects.filter(id=profile_right)
        
        if profile_left==profile_right:
            return Response("a recursive profile connection cannot be established. You must enter different ids.", status=status.HTTP_400_BAD_REQUEST)
        
        if len(profile_validate_left)==0 or len(profile_validate_right)==0:
            return Response("some of the provided profiles do not exist.", status=status.HTTP_404_NOT_FOUND)
                           
        G = nx.Graph()
        vertices=Profile.objects.all()
        source=Profile.objects.get(id=request.data['source'])
        tarjet=Profile.objects.get(id=request.data['tarjet'])
        
        for vertice in vertices:
            G.add_node(vertice)            
            edges=Interaction.objects.all()
            for edge in edges:
                G.add_edge(edge.profile_right,edge.profile_left,weight=1)
            
        G.remove_edges_from(nx.selfloop_edges(G))
        try:
            lange= nx.shortest_path(G,source ,tarjet)
            serializer = ProfileSerializers(lange, many=True)
            return Response(serializer.data)
        except nx.NetworkXNoPath:
            return Response("there is no possible path for the provided profiles.", status=status.HTTP_404_NOT_FOUND)

                              
class Clean_database_APIView(APIView):
    def delete(self, request, format=None):
        Interaction.objects.all().delete()
        Profile.objects.all().delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        
 
            
            
                
                
            

    
        