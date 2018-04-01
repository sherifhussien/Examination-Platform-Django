from import_export import resources

from .models import *


class ExamResource(resources.ModelResource):
    class Meta:
        model = Exam
        fields = ['id', 'title', 'isRandom', 'numberOfQuestions', 'timeLimitInSeconds']


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
        fields = ['id', 'exam', 'questionText', 'pointsForCorrectAnswer','hasModel','model']


class AnswerResource(resources.ModelResource):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answerText', 'isCorrect']

class ScoreResource(resources.ModelResource):
    class Meta:
        model = Score
        fields = ['id', 'score']