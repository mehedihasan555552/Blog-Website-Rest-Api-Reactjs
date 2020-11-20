from rest_framework import serializers
from .models import *
from user.serializer import *



class BlogTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogTags
        fields='__all__'


class BlogSerializer(serializers.ModelSerializer):
    tags = BlogTagsSerializer(many=True)
    author = UserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    class Meta:
        model=Blog
        fields='__all__'



class BlogCommentsSerializer(serializers.ModelSerializer):
    blog=BlogSerializer(read_only=True)
    blog_id=serializers.IntegerField(write_only=True)
    author=UserSerializer(read_only=True)
    author_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=BlogComments
        fields='__all__'
