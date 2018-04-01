from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Exam, Question, Answer, Score
from .resources import *

# Register your models here.
class ExamAdmin(ImportExportModelAdmin):
    resource_class = ExamResource

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

class AnswerAdmin(ImportExportModelAdmin):
    resource_class = AnswerResource

class ScoreAdmin(ImportExportModelAdmin):
    resource_class = ScoreResource

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

admin.site.register(Score,ScoreAdmin)

