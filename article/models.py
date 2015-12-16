from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    body = models.TextField()
    comment = models.TextField()
    like = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

