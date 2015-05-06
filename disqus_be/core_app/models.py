"""This module contains DB models"""
from django.db import models
import datetime


class Comment(models.Model):

    """
    Comments models.
    Stores data about comment for specific site.
    """
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    # Site's url
    url = models.CharField(max_length=50)
    # Author of comment
    title = models.CharField(max_length=50)
    # Email of author
    email = models.CharField(max_length=50)
    # Comment body
    comment = models.TextField()
    # Comment add timestamp
    timestamp = models.DateTimeField(auto_now_add=True)
    # OPTIONAL: email for reply
    replyTo = models.CharField(max_length=256, null=True)

    def __unicode__(self):
        return "{0}: {1}".format(self.author, self.body)
