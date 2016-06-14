from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# The root of our API refers to 'user-list' and 'snippet-list'.
# Our snippet serializer includes a field that refers to 'snippet-highlight'.
# Our user serializer includes a field that refers to 'snippet-detail'.
# Our snippet and user serializers include 'url' fields that by default
# will refer to '{model_name}-detail', which in this case will be
# 'snippet-detail' and 'user-detail'

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
])

urlpatterns = format_suffix_patterns(urlpatterns)

#Adds login and logout functionality for browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]