from django.db import models
from django.contrib import admin


# Create your models here.


class Blogpost(models.Model):

    def __str__(self):
        return self.blog_heading

    blog_heading = models.CharField(max_length=200)
    blog_text = models.TextField(max_length=20000, default="Text")
    pub_date = models.DateTimeField("date published")
    description = models.CharField(max_length=200, default="Description")
