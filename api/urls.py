from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter
from .views import *

from rest_framework import routers
router = DefaultRouter()
#router = routers.SimpleRouter()
router.register('blogs', BlogView)
router.register('blogs-comments', BlogCommentsView)
router.register('blogsTag', BlogTagsView)

urlpatterns = [

    path('', include(router.urls)),
]
