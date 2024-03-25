from django.db import models


# Code Credit: Dennis Ivy (Link in README)
class Category(models.Model):
    """
    Stores multiple categories
    """
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Photo(models.Model):
    """
    Stores a single photo
    """
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.description
    