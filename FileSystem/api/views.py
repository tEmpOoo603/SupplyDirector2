import os

from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import FileSerializer, FolderSerializer
from api.utils import get_content_type
from main.models import File, Folder


class FileView(APIView):
    def get(self, *args, **kwargs):
        try:
            name = kwargs.get('file_name')
            file_instance = File.objects.get(name=name)
            file_path = file_instance.file.path
            response = HttpResponse(open(file_path, 'rb').read())
            response['Content-Disposition'] = f'inline; filename="{name}"'
            response['Content-Type'] = get_content_type(file_path)
            return response
        except File.DoesNotExist:
            return Response({'error': 'File not found'})
        except Exception as e:
            return Response({'error': str(e)})

    def post(self, request, *args, **kwargs):
        data = request.data
        folder = kwargs.get('folder_name')
        if folder:
            folder = Folder.objects.get(name=folder).id
            data['folder'] = folder
        data['name'] = kwargs.get('file_name')
        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Файл успешно загружен'})
        else:
            return Response({'Ошибка': "Ошибка при загрузке файла"})

    def delete(self, *args, **kwargs):
        file_name = kwargs.get('file_name')
        obj = File.objects.get(name=file_name)
        obj.delete()
        return Response({'message': f"file {file_name} deleted!"})


class FolderView(APIView):
    def get(self, *args, **kwargs):
        folder_name = kwargs.get('folder_name')
        content = Folder.objects.filter(name=folder_name).prefetch_related('subfolders', 'files')
        subfolders = []
        files = []
        main_folder = content.first()
        response = {'folder': main_folder.name}
        for subfolder in main_folder.subfolders.all():
            subfolders.append(subfolder)
        if subfolders:
            folder_serializer = FolderSerializer(subfolders, many=True)
            response['subfolders'] = folder_serializer.data
        for file in main_folder.files.all():
            files.append(file)
        if files:
            file_serializer = FileSerializer(files, many=True)
            response['files'] = file_serializer.data
        return Response(response)

    def post(self, *args, **kwargs):
        data = {}
        parent = kwargs.get('parent_folder_name')
        if parent:
            parent = Folder.objects.get(name=parent).id
            data['parent'] = parent
        data['name'] = kwargs.get('folder_name')
        serializer = FolderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Папка успешно создана'})
        else:
            return Response({'Ошибка': "Ошибка при создании папки"})

    def delete(self, *args, **kwargs):
        folder_name = kwargs.get('folder_name')
        obj = Folder.objects.get(name=folder_name)
        obj.delete()
        return Response({'message': f"file {folder_name} deleted!"})
