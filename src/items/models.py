from django.db import models
from django.conf import settings
from django.urls import reverse
from projects.models import Project
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
class Item(models.Model):
    class ItemStatus(models.TextChoices):
        PUBLISH = 'publish', 'Publish'
        PENDING ='pending', 'Pending'
        DRAFT = 'draft', 'Draft'
        ON_HOLD = 'on_hold', 'On Hold'
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ItemStatus.choices, default=ItemStatus.DRAFT)
    _status = models.CharField(max_length=20, choices=ItemStatus.choices, null=True, blank=True)
    status_changed_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
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
        if self._status != self.status:
            self._status = self.status
            self.status_changed_at = timezone.now()
        super().save(*args, **kwargs)

    def get_prefix(self, trailing_slash=True):
        project_prefix = self.project.get_prefix(trailing_slash=False)
        if trailing_slash:
            return f"{project_prefix}/items/{self.id}/"
        return f"{project_prefix}/items/{self.id}"

    def get_upload_url(self):
        return reverse("items:upload", kwargs={"id": self.id})
    
    def get_files_url(self):
        return reverse("items:files", kwargs={"id": self.id})
        
    def get_absolute_url(self):
        return reverse("items:detail", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("items:delete", kwargs={"id": self.id})
    
    def get_edit_url(self):
        return reverse("items:edit", kwargs={"id": self.id})