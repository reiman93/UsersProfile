from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    #Profile
    path('profile', Profile_APIView.as_view()), 
    path('profile/<int:pk>/', Profile_APIView_Detail.as_view()),
    
    #Interactions
    path('interaction', Profile_Interactions_APIView.as_view()), 
    path('interaction/<int:pk>/', Profile_Interactions_APIView_Detail.as_view()),    
    
    #Graph
    path('frens/<int:pk>/', Graph_APIView.as_view()),    
    path('frens', Graph_edge_APIView.as_view()),    
]