from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
