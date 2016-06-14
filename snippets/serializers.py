from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

#using a hyperlinked relationship between entities.
# The HyperlinkedModelSerializer has the following differences from ModelSerializer:
# It does not include the pk field by default.
# It includes a url field, using HyperlinkedIdentityField.
# Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.

# used to serialize the snippet data
class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


# used to serialize the user data
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')