from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Contents, Thread, Response
from users.serializer import UserSerializer
import re
import hashlib
import datetime
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
            "response_id",
            "thread",
            "created_at",
        )

    def create(self, validated_data):

        def get_client_ip(request):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            return ip

        def base(n, b, digits="0123456789abcdefghijklmnopqrstuvwxyz"):
            if n == 0:
                return '0'
            s = []
            p = abs(n)
            while p:
                s.append(digits[p % b])
                p //= b
            if n < 0:
                s.append('-')
            return ''.join(reversed(s))

        def create_id(ip):
            date = datetime.date.today().strftime('%Y%m%d')
            id_row = ip + date
            id_row = id_row.encode()
            base_16_id = hashlib.md5(id_row).hexdigest()
            base_10_id = int(base_16_id,16)
            response_id = base(base_10_id, 36)[:10]
            return response_id

        response = super(ResponseSerializer, self).create(validated_data)

        response_id = create_id(get_client_ip(self.context["request"]))
        response.response_id = response_id

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
            "response_id",
            "created_at",
            "thread",
            "is_active",
            "is_writable",
        )

    def create(self, validated_data):

        def get_client_ip(request):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            return ip

        def base(n, b, digits="0123456789abcdefghijklmnopqrstuvwxyz"):
            if n == 0:
                return '0'
            s = []
            p = abs(n)
            while p:
                s.append(digits[p % b])
                p //= b
            if n < 0:
                s.append('-')
            return ''.join(reversed(s))

        def create_id(ip):
            date = datetime.date.today().strftime('%Y%m%d')
            id_row = ip + date
            id_row = id_row.encode()
            base_16_id = hashlib.md5(id_row).hexdigest()
            base_10_id = int(base_16_id,16)
            response_id = base(base_10_id, 36)[:10]
            return response_id

        thread = super(ThreadSerializer, self).create(validated_data)

        response_id = create_id(get_client_ip(self.context["request"]))
        thread.response_id = response_id

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
