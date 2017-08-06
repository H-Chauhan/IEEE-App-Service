from django.db import models
from django.contrib.auth.models import User

class News(models.Model):

    def __str__(self):
        return self.body[:50]

    publishedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    heading = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    postedBy = models.ForeignKey('Coordinator', on_delete=models.CASCADE)

class Coordinator(models.Model):

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.BigIntegerField()