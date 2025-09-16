
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=120)
    email = models.EmailField()
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Comment by {self.name} on {self.post.title}"
