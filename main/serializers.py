from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    created_at_humanized = serializers.CharField()

    class Meta:
        model = models.Review
        fields = '__all__'
