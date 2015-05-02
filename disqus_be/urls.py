"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from core_app.api import CommentResource

v1_api = Api(api_name='v1')
v1_api.register(CommentResource())

urlpatterns = patterns(
    '',
    url(r'^api/', include(v1_api.urls)),	# Pattern that will be used for identification of API
)
