from rest_framework import viewsets
from .serializers import JobSerializer, JobReviewSerializer
from .models import Job, JobReview
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from job.serializers import JobSerializer, JobReviewSerializer, searchSerializer
from job.models import Job, JobReview
from upload import upload_image

from note.models import Note
from photo.models import Photo

class JobAPI(viewsets.ModelViewSet):
    queryset = Job.objects.prefetch_related('reviews').all()
    serializer_class = JobSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        images = request.FILES.get("image")
        url = upload_image(images, "job")

        serializer = self.get_serializer(data=request.data)

        serializer.image = url

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def AllSearch(self, request):
        search = request.query_params.get('search')
        if not search:
            return Response("Search parameter 'search' is required.", status=status.HTTP_400_BAD_REQUEST)

        job_results = Job.objects.filter(tag__icontains=search) | Job.objects.filter(title__icontains=search) | Job.objects.filter(content__icontains=search)
        note_results = Note.objects.filter(tag__icontains=search) | Note.objects.filter(title__icontains=search) | Note.objects.filter(content__icontains=search)
        photo_results = Photo.objects.filter(tag__icontains=search)

        search_results = list(job_results) + list(note_results) + list(photo_results)

        serializer = searchSerializer(search_results, many=True, context={'request': request})

        return Response(serializer.data)

class JobReviewsAPI(viewsets.ModelViewSet):
    queryset = JobReview.objects.all()
    serializer_class = JobReviewSerializer
    


# Create your views here.
