from django.urls import path
from .views import PhotoAPI, PhotoDateAPI 

urlpatterns = [
    path('api/', PhotoAPI.as_view({'get': 'list', 'post': 'create'}), name='photo-list'),
    path('api/<date:date>/', PhotoDateAPI.as_view(), name='photo-by-date'),  
]
