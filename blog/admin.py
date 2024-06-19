from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "slug")
    prepopulated_fields = {"slug": ("title",)} #cant have both prepopulated and readonly field

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
