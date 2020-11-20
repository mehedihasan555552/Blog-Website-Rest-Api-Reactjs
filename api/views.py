from django.shortcuts import render
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer


class BlogCommentsView(ModelViewSet):
    queryset = BlogComments.objects.all()
    serializer_class=BlogCommentsSerializer



class BlogTagsView(ModelViewSet):
    queryset = BlogTags.objects.all()
    serializer_class=BlogTagsSerializer
