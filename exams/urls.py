from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', ExamList.as_view()),
    path('submit/', PostGrade.as_view()),
    # path('submit/', postGrade),

]