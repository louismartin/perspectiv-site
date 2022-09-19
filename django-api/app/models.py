from django.db import models
from django.contrib.auth.models import User


class TargetAllocation(models.Model):
    target_index = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
