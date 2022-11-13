from django.db import models


class Post(models.Model):
    text = models.TextField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
