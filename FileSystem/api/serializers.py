from rest_framework import serializers

from main.models import File, Folder


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'folder']


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent']
