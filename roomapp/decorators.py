from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render

from roomapp.models import Room


def room_ownership_required(func):
    def decorated(request, *args, **kwargs):
        room = Room.objects.get(pk=kwargs['pk'])
        if not room.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
