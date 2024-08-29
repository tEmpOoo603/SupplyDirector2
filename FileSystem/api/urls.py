from django.urls import path

from api.views import *

urlpatterns = [
    path('folder/<str:folder_name>/', FileDownloadView.as_view()),   # display folder
    path('folder/create/<str:folder_name>/', FileDownloadView.as_view()),   # create folder in root folder
    path('folder/<str:folder_name>/create-folder/<str:folder_name_create>/', FileDownloadView.as_view()),   # create folder in another folder
    path('folder/delete/<str:folder_name>/', FileDownloadView.as_view()),   # delete folder
    path('file/<str:file_name>/', FileDownloadView.as_view()),   # display file
    path('file/create/<str:file_name>/', FileDownloadView.as_view()),   # create file in root folder
    path('folder/<str:folder_name>/create-file/<str:file_name>/', FileDownloadView.as_view()),   # create file in another folder
]