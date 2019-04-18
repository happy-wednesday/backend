from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from hwd import settings

class Contents(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー',
        related_name='user', on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0),
                    MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

class Thread(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー',
        related_name='thread_user', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.TextField()
    #message = models.TextField()
    #response_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_writable = models.BooleanField(default=True)


class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー',
        related_name='response_user', on_delete=models.SET_NULL, blank=True, null=True)
    thread = models.ForeignKey(Thread, verbose_name='スレッド',
        related_name='thread', on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    response_id = models.TextField(blank=True, null=True)
    response_number = models.IntegerField(default=0)
    anchor_parent = models.ManyToManyField("self", related_name='anchor_child', blank=True, null=True, symmetrical=False)
    is_parent = models.BooleanField(default=False)
    is_child = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
