from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images", null=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        "Author", on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
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
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    comment = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Tag(models.Model):
    caption = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.caption
