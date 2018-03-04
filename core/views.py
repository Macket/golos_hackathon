# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
from rest_framework.views import APIView
from backend import User

VIDOS = 'test-video'
VIDOS_PATH = '/home/ivan/'

class ExampleView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        vidos_metadata = User.get_video_unauthorized(VIDOS, VIDOS_PATH)
        return Response(vidos_metadata)


class IndexView(TemplateView):

    template_name = 'core/index.html'
