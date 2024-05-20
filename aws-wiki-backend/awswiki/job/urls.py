from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobAPI, JobReviewsAPI

# Create routers for each of the viewsets
Job_router = DefaultRouter()
Job_router.register(r'api', JobAPI, basename='Job')

Job_reviews_router = DefaultRouter()
Job_reviews_router.register(r'api', JobReviewsAPI, basename='Job_review')

# URL patterns that include the routers
urlpatterns = [
    path('', include(Job_router.urls)),
    path('review/', include(Job_reviews_router.urls)),
]
