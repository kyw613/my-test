from rest_framework import serializers
from .models import Job, JobReview

class JobReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobReview
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    reviews = JobReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'


class searchSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    tag = serializers.CharField()
    title = serializers.CharField(required=False)
    writer = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    date = serializers.DateTimeField()
    image = serializers.FileField()