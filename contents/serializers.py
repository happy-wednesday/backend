from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Contents, Thread, Response
from users.serializer import UserSerializer
import re
#from rest_framework.fields import CurrentUserDefault

class ContentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Contents
        fields = (
            'id',
            "user",
            'comment',
            "rating",
            'created_at'
        )

    def create(self, validated_data):
        contents = super(ContentsSerializer, self).create(validated_data)
        user = self.context['request'].user
        if not user.is_anonymous:
            contents.user = user
        contents.save()
        return contents

class ResponseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Response
        fields = (
            "id",
            "user",
            "message",
            "thread",
            "created_at",
        )

    def create(self, validated_data):
        response = super(ResponseSerializer, self).create(validated_data)
        user = self.context['request'].user
        if not user.is_anonymous:
            response.user = user

        r_message = validated_data["message"].replace("\n", "<br>")
        pattern = r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)"
        repatter = re.compile(pattern)
        result = repatter.findall(r_message)
        for urls in result:
            url = "".join(urls)
            print(url)
            r_message = r_message.replace(url, f'<a href="{url}" target="_blank">{url}</a>')
        response.message = r_message
        response.save()
        return response

class ThreadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    thread = ResponseSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = (
            "id",
            "user",
            "title",
            "message",
            "created_at",
            "thread",
            "is_active",
            "is_writable",
        )

    def create(self, validated_data):
        thread = super(ThreadSerializer, self).create(validated_data)
        user = self.context['request'].user
        if not user.is_anonymous:
            thread.user = user

        r_message = validated_data["message"].replace("\n", "<br>")
        pattern = r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)"
        repatter = re.compile(pattern)
        result = repatter.findall(r_message)
        for urls in result:
            url = "".join(urls)
            print(url)
            r_message = r_message.replace(url, f'<a href="{url}" target="_blank">{url}</a>')
        thread.message = r_message
        thread.save()
        return thread
