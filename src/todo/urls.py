from django.urls import re_path, include
from todo import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
  re_path(r'^', include(router.urls)),
]

