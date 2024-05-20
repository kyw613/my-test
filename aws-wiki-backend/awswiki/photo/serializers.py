from rest_framework import serializers

from .models import Photo, PhotoReview

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoReview
        fields = '__all__'
