from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from PIL import Image
from PIL import ImageOps
import glob, os
from django.core.urlresolvers import reverse

class UploadsManager(models.Manager):
    def create_upload(self, upload_obj):
        upload = self.create(upload_obj)
        # return the primary key
        return upload

class Upload(models.Model):
    image_path = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User)
    confidence_score = models.CharField(max_length=200, null=True)
    tensor_verdict = models.CharField(max_length=100, null=True)
    added_on = models.DateField(auto_now_add=True)
    # This might be helpful?
    title = models.CharField(max_length=140, null=True)
    accurate = models.CharField(max_length=50, null=True)
    # views = models.IntegerField(default=0)
    # upvotes = models.PositiveIntegerField(default=0)
    # downvotes = models.PositiveIntegerField(default=0)

    objects = UploadsManager()

    def get_absolute_url(self):
        return reverse('Media:gallery', args=[str(self.id)])

    def __unicode__(self):
        return self.image_path
