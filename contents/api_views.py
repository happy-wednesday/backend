from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
#from rest_framework.permissions import AllowAny
from .models import Contents, Thread, Response
from .serializers import ContentsSerializer, ThreadSerializer, ResponseSerializer
from django.db.models import Prefetch


class ContentsViewSet(ModelViewSet):
    #permission_classes = (AllowAny,)
    serializer_class = ContentsSerializer
    queryset = Contents.objects.order_by("-created_at")

class ThreadViewSet(ModelViewSet):
    #permission_classes = (AllowAny,)
    serializer_class = ThreadSerializer
    queryset = Thread.objects.order_by("-created_at").prefetch_related(Prefetch('thread',
        queryset=Response.objects.order_by('created_at')))

class ResponseViewSet(ModelViewSet):
    #permission_classes = (AllowAny,)
    serializer_class = ResponseSerializer
    queryset = Response.objects.order_by("-created_at")
