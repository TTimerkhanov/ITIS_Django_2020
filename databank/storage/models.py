import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


def item_photo_path(instance, filename):
    uuid_salt = uuid.uuid4()
    return f"items/{uuid_salt}-{filename}"


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey('Source', related_name='items', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=item_photo_path, max_length=120)

    def __str__(self):
        return f"Item: {self.name} from {self.source.name}"

    def get_absolute_url(self):
        return reverse('storage:item-detail', kwargs={'pk': self.pk})


class Source(models.Model):
    url = models.URLField(verbose_name="URL")
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.url})"
