from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)

