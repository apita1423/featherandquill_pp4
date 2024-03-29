from django.db import models
from cloudinary.models import CloudinaryField


# Code Credit: I Think Therefore I Blog Walkthrough
class About(models.Model):
    """
    Stores a single about us text
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
