from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.




class SampleView(APIView):
    
    def get(self, request):
        return Response({'message': 'GET.............Hello World!'}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({'message': 'POST............Hello World!'}, status=status.HTTP_200_OK)