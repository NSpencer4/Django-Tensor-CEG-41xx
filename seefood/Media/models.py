from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from PIL import Image
from PIL import ImageOps
import glob, os
from django.core.urlresolvers import reverse

class Upload(models.Model):
    image_path = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    confidence_score = models.CharField(max_length=200)
    added_on = models.DateField(auto_now_add=True)
    # This might be helpful?
    title = models.CharField(max_length=140)
    # views = models.IntegerField(default=0)
    # upvotes = models.PositiveIntegerField(default=0)
    # downvotes = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('Media:gallery', args=[str(self.id)])

    # Older python version
    # def __str__(self):
    #     return self.image_path

    # Older python 3 way
    def __unicode__(self):
        return self.image_path
