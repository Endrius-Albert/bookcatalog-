from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class RootView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the BookCatalog API"})

class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"})

class BookView(APIView):
    def get(self, request):
        return Response({"hello": "django"})

