from django.core.validators import MinLengthValidator
from django.db import models


class Review(models.Model):
    username = models.CharField(
        max_length=32,
        validators=[MinLengthValidator(3)]
    )
    text = models.CharField(
        max_length=512,
        validators=[MinLengthValidator(16)]
    )
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
