from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

from frontend.models import *
class role(models.Model):
    users = models.ManyToManyField(User)
    USER_ROLE_CHOICES = (
        ('user', 'User'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
        ('developer', 'Developer'),
        ('editor', 'Editor'),
    )
    name = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)
    def __str__(self):
        return self.name
class Event(models.Model):
    INVITATION_CHOICES = [
        ('wedding_invites', 'Wedding Invites'),
        ('other_event_invites', 'Other Event-based Invites'),
        ('stationeries', 'Stationeries'),
    ]

    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    invitation_type = models.CharField(max_length=50, choices=INVITATION_CHOICES)

    def __str__(self):
        return self.title