from django.urls import path

from api.views import *

urlpatterns = [
    path('folder/<str:folder_name>/', FolderView.as_view()),   # delete by delete-method, get by get-method, create by post-method
    path('folder/<str:parent_folder_name>/<str:folder_name>/', FolderView.as_view()),   # create folder in another folder - post
    path('folder/<str:folder_name>/create-file/<str:file_name>/', FileView.as_view()),   # create file in folder - post
    path('file/<str:file_name>/', FileView.as_view()),   # delete by delete-method, get by get-method
]