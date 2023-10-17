from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    date_of_registration = models.DateField(auto_now_add=True)
    bio = models.TextField(max_length=500, blank=True)
    age = models.IntegerField()

    class Meta:
        ordering = ['username']
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name="age_gte_18"),
        ]

