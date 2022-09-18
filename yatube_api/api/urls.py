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
    # { 111
    #     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzU5MjQ3MywianRpIjoiNmQ0ZDM2NjY1NGJiNDAzZjg1N2U0MTBkYTBjOWUxYmYiLCJ1c2VyX2lkIjoxfQ.G7mLC8FK7hAFYXM2__F1P3kvpwhLXvrrQ34-0amIWLI",
    #     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNzY1MjczLCJqdGkiOiJiMjY5MGIwYjg0NTE0YjY1YjM3N2QxMWVmZGJjMjRlYyIsInVzZXJfaWQiOjF9.v8JHs3lPjRPX0BYfRTXdYA2wMuaqmyL5u157HF5dDvQ"
    # }
    # { 222
    #     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzU5MjU2MiwianRpIjoiNjMwODI5MzViZjY3NDk1YTg2OGFlOTJmYzc3N2VhYTEiLCJ1c2VyX2lkIjoyfQ.ICwNtKzUbOLDxXd1518d6-QYmhjeruk8RIWETGx7Mmc",
    #     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNzY1MzYyLCJqdGkiOiIyYTBlMzQ1ZmI3ZjA0ZGEyODBmNzhlYjVlY2FjZjJkOSIsInVzZXJfaWQiOjJ9.1G2NFXraD1n3zqYnmNseWtNHoendv2CiPdx0rtRUAQk"
    # }
]
