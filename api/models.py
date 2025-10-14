from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    groups = models.ManyToManyField(
        Group, blank=True, related_name="api_user_groups", related_query_name="user"
    )
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="api_user_permissions", related_query_name="user"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
class Feed(models.Model):

    text_content = models.TextField(blank=True, null=True)

    is_hidden = models.BooleanField(default=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feeds')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)



class FeedImage(models.Model):

    image_url = models.URLField()

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)



class Comment(models.Model):

    text_content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)



class Report(models.Model):

    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='reports')

    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:

        unique_together = ('reporter', 'feed')



class Logging(models.Model):

    endpoint = models.CharField(max_length=255)

    method = models.CharField(max_length=10)

    status_code = models.IntegerField()

    error_message = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)