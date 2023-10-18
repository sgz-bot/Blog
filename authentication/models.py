from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
# Create your models here.

