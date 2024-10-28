from django.db import models
from django.conf import settings
from django.urls import reverse
from projects.models import Project

User = settings.AUTH_USER_MODEL

# Create your models here.
class Item(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, related_name="items_added", on_delete=models.SET_NULL, null=True)
    added_by_username = models.CharField(max_length=150, null=True, blank=True)
    last_modified_by = models.ForeignKey(User, related_name="items_changed", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_username = self.added_by.username
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("items:detail", kwargs={"id": self.id})
    