"""This module contains API resource classes"""
from tastypie.resources import ModelResource, ALL
from core_app.models import Comment
from tastypie.authorization import Authorization
from tastypie import fields
from core_app import utils


class CommentResource(ModelResource):

    """
    Comment's resource class for API
    """
    class Meta:
        # Object class of resource
        object_class = Comment
        # Fields that must by used
        fields = ['url', 'title', 'email', 'comment', 'replyTo', 'timestamp']
        # Method that will get objects collection
        queryset = Comment.objects.all()
        # Resource name that will be used while usage
        resource_name = 'comment'
        # Authorization method (Currently always authorized)
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'url': ['exact', 'iexact']
        }

    def alter_list_data_to_serialize(self, request, data):
        if request.GET.get('total_count'):
            return {'total_count': data['meta']['total_count']}
        return data
