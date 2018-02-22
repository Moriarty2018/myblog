from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Mycomment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('myblog.Article')

    def __str__(self):
        return self.text[:20]