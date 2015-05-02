"""This module contains DB models"""
from django.db import models
from django.utils import timezone
from core_app import utils
from hashlib import md5
import datetime


class Comment(models.Model):
    """
    Comments models.
    Stores data about comment for specific site.
    """
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    author = models.CharField(max_length=50)                # Author of comment
    email = models.CharField(max_length=50)                 # Email of author
    timestamp = models.DateTimeField(auto_now_add=True)     # Comment add timestamp
    host = models.CharField(max_length=50)                  # Site's hostname
    body = models.TextField()                               # Comment body
    replyTo = models.CharField(max_length=50, null=True)    # OPTIONAL: email for reply

    def __unicode__(self):
        return "{0}: {1}".format(self.author, self.body)
