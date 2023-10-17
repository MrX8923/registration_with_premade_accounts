from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    email = models.EmailField(
        unique=True,
    )
    date_of_registration = models.DateField(
        auto_now_add=True,
        verbose_name='Дата регистрации',
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='О себе',
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Возраст',
    )
    age_18 = models.BooleanField(
        default=True,
        verbose_name='18+',
    )

    class Meta:
        ordering = ['username']
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__gte=18),
                name="age_gte_18",
            ),
        ]
        verbose_name = 'User'
        db_table = 'user_profile'
