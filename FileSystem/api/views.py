import os

from django.http import FileResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.views import APIView

from main.models import File



class FileDownloadView(APIView):
    def get(self, request, name):
        pass