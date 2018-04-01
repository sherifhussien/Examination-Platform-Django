from .models import *
from rest_framework import serializers, fields


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answerText', 'isCorrect', 'timestamp', 'updated')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'questionText', 'pointsForCorrectAnswer', 'hasModel', 'model', 'timestamp', 'updated','answers')


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Exam
        fields = ('id', 'title', 'isRandom', 'numberOfQuestions', 'timeLimitInSeconds', 'timestamp', 'updated' ,'questions')



class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('id','score', 'timestamp', 'updated')

    def create(self, validated_data):
        return Score.objects.create(**validated_data)