from rest_framework import serializers
from .models import StudyPost


class StudyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPost
        fields = "__all__"
