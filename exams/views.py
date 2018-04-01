from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.utils.six import BytesIO

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from .models import *
from .serializers import *


from rest_framework.views import APIView

# Create your views here.
class ExamList(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class PostGrade(APIView):
    def post(self, request, format=None):
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = ScoreSerializer(data=data)
        serializer.is_valid()
        serializer.validated_data
        user = serializer.save()

        data = {}
        data['userId'] = user.id
        
        return Response(data)