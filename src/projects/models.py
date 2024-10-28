from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from home.utils.generators import unique_sulgify
from .validators import validate_project_handle

User = settings.AUTH_USER_MODEL

class AnonymousProject():
    value = None
    is_activated = False

class Project(models.Model):
    owner = models.ForeignKey(User, null=True, related_name='owner_projects', on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, null=True)
    handle = models.SlugField(null=True, blank=True, unique=True, validators=[validate_project_handle])
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, related_name="projects_added", on_delete=models.SET_NULL, null=True)
    added_by_username = models.CharField(max_length=150, null=True, blank=True)
    last_modified_by = models.ForeignKey(User, related_name="projects_changed", on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"handle": self.handle})
    
    def get_delete_url(self):
        return reverse("projects:delete", kwargs={"handle": self.handle})
    
    def get_activate_url(self):
        return reverse("projects:activate", kwargs={"handle": self.handle})
    
    @property
    def is_activated(self):
        return True

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_username = self.added_by.username
        if not self.handle:
            self.handle = unique_sulgify(self, slug_field="handle", invalid_slug="create")
        super().save(*args, **kwargs)
