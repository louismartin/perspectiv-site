from django.db import models
from django.contrib.auth.models import User


class BudgetInsightUser(models.Model):
    app_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100)