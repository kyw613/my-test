from rest_framework import serializers
from .models import Note, NoteReview

class NoteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteReview
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    reviews = NoteReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
