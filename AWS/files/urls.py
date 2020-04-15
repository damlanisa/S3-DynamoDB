from django.urls import path
from . import views


urlpatterns = [
    path('', views.UploadView.as_view(), name='file-upload'),
    path('dynamoDB', views.dynamoDB, name='dynamoDB'),
]
