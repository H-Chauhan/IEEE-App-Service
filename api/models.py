from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isApproved = models.BooleanField(default=False)
    mobile = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class News(models.Model):
    publishedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    heading = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    publishedBy = models.ForeignKey('Member', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body[:50]

    class Meta:
        ordering = ['-publishedOn']
        verbose_name_plural = "News"


class SIG(models.Model):
    topic = models.CharField(max_length=100)
    date = models.DateField()
    fromTime = models.TimeField()
    toTime = models.TimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    coordinators = models.ManyToManyField(Member)

    def __str__(self):
        return self.topic

    def get_coordinator(self):
        return self.member_set.all()

    class Meta:
        ordering = ['-date', 'fromTime']

class Event(models.Model):
    name = models.CharField(max_length=100)
    fromDateTime = models.DateTimeField()
    toDateTime = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    coordinators = models.ManyToManyField(Member)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-fromDateTime']

class CouncilMember(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    fbProfileLink = models.URLField()
