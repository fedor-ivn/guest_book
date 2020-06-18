from rest_framework.generics import ListCreateAPIView

from . import models
from . import serializers


class ReviewAPIView(ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
