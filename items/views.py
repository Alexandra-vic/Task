from django.shortcuts import render
from django.urls.conf import include 


from . serializers import ItemsSerializer
from . models import Items


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.http import Http404


class ItemsList(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class ItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer




