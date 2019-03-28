from rest_framework.routers import DefaultRouter
from . import api_views


contents_router = DefaultRouter()
contents_router.register(r'', api_views.ContentsViewSet)

thread_router = DefaultRouter()
thread_router.register(r'', api_views.ThreadViewSet)

response_router = DefaultRouter()
response_router.register(r'', api_views.ResponseViewSet)
