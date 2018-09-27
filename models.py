from django.db import models
from django.utils import timezone


class Container(models.Model):
    """Container data."""

    name = models.CharField(max_length=50)
    ssh_key = models.TextField()
    update_avaliable = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
