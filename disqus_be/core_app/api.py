"""This module contains API resource classes"""
from tastypie.resources import ModelResource
from core_app.models import Comment
from tastypie.authorization import Authorization
from tastypie import fields
from core_app import utils


class CommentResource(ModelResource):
	"""
	Comment's resource class for API
	"""
    class Meta:
        object_class = Comment 													# Object class of resource
        fields = ['author', 'email', 'host', 'text', 'replyTo', 'timestamp'] 	# Fields that must by used
        queryset = Comment.objects.all() 										# Method that will get objects collection
        resource_name = 'comment' 												# Resource name that will be used while usage
        authorization = Authorization() 										# Authorization method (Currently always authorized)
        always_return_data = True