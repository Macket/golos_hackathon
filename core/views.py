# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import VideoSerializer
from backend import User

VIDOS = 'videopotest'
VIDOS_PATH = '/Users/alexander/Developer/startup_hack/golos_hackathon/static/_videos/tmp-video.mp4'


class ExampleView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        name = self.request.query_params.get('name')
        if name:
            return Response(User.get_video_unauthorized(name, VIDOS_PATH))
        return Response({})


class VideoViewSet(APIView):

    def get(self, request, format=None):
        videos_list = User.get_videos_list('')
        print(videos_list)
        return Response(videos_list)


class IndexView(TemplateView):

    template_name = 'core/index.html'
