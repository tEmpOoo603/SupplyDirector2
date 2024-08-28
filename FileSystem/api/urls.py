from django.urls import path

urlpatterns = [
    path('folder/<str:folder_name>/'),   # display folder
    path('folder/create/<str:folder_name>/'),   # create folder in root folder
    path('folder/<str:folder_name>/create-folder/<str:folder_name_create>/'),   # create folder in another folder
    path('folder/delete/<str:folder_name>/'),   # delete folder
    path('file/<str:file_name>/'),   # display file
    path('file/create/<str:file_name>/'),   # create file in root folder
    path('folder/<str:folder_name>/create-file/<str:file_name>/'),   # create file in another folder
]