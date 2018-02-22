from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Category(models.Model):
    cname = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.cname



@python_2_unicode_compatible
class Tag(models.Model):
    tname = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.tname


@python_2_unicode_compatible
class Article(models.Model):
    atitle = models.CharField(max_length=40)
    abody = models.TextField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    zhaiyao = models.CharField(max_length=150,blank=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag,blank=True)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.atitle

    def get_url(self):
        return reverse('myblog:detail',kwargs={'pk':self.pk})