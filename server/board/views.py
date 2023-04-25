from rest_framework import viewsets
from .models import StudyPost
from .serializers import StudyPostSerializer


class StudyPostViewSet(viewsets.ModelViewSet):
    queryset = StudyPost.objects.all()
    serializer_class = StudyPostSerializer
