from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from .models import Photo
from .serializers import PhotoSerializer
from upload import upload_image

class PhotoAPI(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        images = request.FILES.get("image")
        url = upload_image(images, "photo")

        serializer = self.get_serializer(data=request.data)

        serializer.image = url

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoDateAPI(APIView):
    def get(self, request, date, format=None):
        photos = Photo.objects.filter(date__date=date)
        if not photos.exists():
            return Response({"message": "No photos found for this date"}, status=404)
        serializer = PhotoSerializer(photos, many=True, context={'request': request})
        return Response(serializer.data)
