from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import NoteSerializer, NoteReviewSerializer
from .models import Note, NoteReview
from upload import upload_image

class NoteAPI(viewsets.ModelViewSet):
    queryset = Note.objects.prefetch_related('reviews').all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        images = request.FILES.get("image")
        url = upload_image(images, "note")

        serializer = self.get_serializer(data=request.data)

        serializer.image = url

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteReviewsAPI(viewsets.ModelViewSet):
    queryset = NoteReview.objects.all()
    serializer_class = NoteReviewSerializer
