from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from PIL import Image
from PIL import ImageOps
import glob, os
from django.core.urlresolvers import reverse

class Post(models.Model):


    added_on = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=140)
    views = models.IntegerField(default=0)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes=  models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('Media:gallery', args=[str(self.id)])

    def score(self):
        return self.upvotes - self.downvotes

    def __str__(self):
        return self.title



class Photo(models.Model):

    file = models.ImageField(upload_to='photos')
    thumb = models.ImageField(upload_to='thumbnails', editable=False)
    post = models.ForeignKey('Post', related_name="photos")


    def __str__(self):
        return self.post.title

    def _create_thumbnail(self):
        #Create thumbnails by cropping a square of the full image
        from django.conf import settings
        from django.core.files import File
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        size = {'width':180, 'height':180}
        #open original image and get length and width
        im = Image.open(os.path.join(settings.MEDIA_ROOT, self.file.name))
        im_width = im.size[0]
        im_length = im.size[1]
        im = ImageOps.fit(im,(size['width'], size['height']) ,0, (0.5, 0.5))


        #Save new image to thumb field
        temp_handle = StringIO()
        im.save(temp_handle, 'jpeg')
        temp_handle.seek(0)
        suf = SimpleUploadedFile(
        os.path.split(self.file.name)[-1],
        temp_handle.read(),
        content_type='image')
        self.thumb.save(suf.name, suf, save=False)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        self._create_thumbnail()
        super(Photo, self).save(*args, **kwargs)
        #self.save()


class Comment(models.Model):
    #item = generic relation back to album or post
    post = models.ForeignKey('Post', related_name="comments")
    owner = models.ForeignKey(User)
    comments = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.comments[:20]
