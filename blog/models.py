from django.db import models
from django.utils.timezone import now

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="posts", null=True)
    tags = models.ManyToManyField("Tag", related_name="posts")
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    
    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
class Tag(models.Model):
    caption = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.caption