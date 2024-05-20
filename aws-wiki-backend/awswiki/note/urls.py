from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteAPI, NoteReviewsAPI

# Create routers for each of the viewsets
Note_router = DefaultRouter()
Note_router.register(r'api', NoteAPI, basename='Note')

Note_reviews_router = DefaultRouter()
Note_reviews_router.register(r'api', NoteReviewsAPI, basename='Note_review')

# URL patterns that include the routers
urlpatterns = [
    path('', include(Note_router.urls)),
    path('review/', include(Note_reviews_router.urls)),
]
