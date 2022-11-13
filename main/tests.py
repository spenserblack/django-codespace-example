from django.test import TestCase

from .models import Post


class TestPosts(TestCase):
    def test_create_post(self):
        self.client.post("/", {"text": "test"})
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().text, "test")
