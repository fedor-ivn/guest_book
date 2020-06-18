from rest_framework import filters
from rest_framework.generics import ListCreateAPIView

from . import models
from . import serializers


class ReviewAPIView(ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'created_at']
