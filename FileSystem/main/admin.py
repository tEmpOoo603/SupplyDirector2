from django.contrib import admin

from main.models import Folder, File


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'parent']
    search_fields = ['id', 'name']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'folder', 'file']
    search_fields = ['id', 'name']
