from django.db import models
from .validators import validate_file_extension


def model_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/models/exam_<id>/<filename>
    return 'models/exam_{0}/{1}'.format(instance.exam.id, filename)

# Create your models here.
class Exam(models.Model):
    title                   = models.CharField(max_length=120, null = False, blank = False, unique = True)
    isRandom                = models.BooleanField(null = False, blank = False)
    numberOfQuestions       = models.PositiveIntegerField(default = 0)
    timeLimitInSeconds      = models.PositiveIntegerField(default = 0)
    timestamp               = models.DateTimeField(auto_now_add = True) #automatically set the field to now every time the object is first created
    updated                 = models.DateTimeField(auto_now = True) #automatically set the field to now every time the object is saved

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_MODELS =[
            ('Sphere','Sphere'),
            ('Cube','Cube')
            ]
    exam                    = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    questionText            = models.CharField(max_length=200, null = False, blank = False)
    pointsForCorrectAnswer  = models.PositiveIntegerField(null = False, blank = False)
    hasModel                = models.BooleanField(null = False, blank = False)
    model                   = models.CharField(max_length=50, choices=QUESTION_MODELS, null=True, blank=True)
#   model                   = models.FileField(upload_to=model_directory_path, validators=[validate_file_extension], null=True, blank=True)  #.name to access file directory .url is better
    timestamp               = models.DateTimeField(auto_now_add = True) 
    updated                 = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.questionText + " for exam : " + self.exam.title


class Answer(models.Model):
    question      = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answerText    = models.CharField(max_length=200, null = False, blank = False)
    isCorrect     = models.BooleanField(null = False, blank = False)
    timestamp     = models.DateTimeField(auto_now_add = True) 
    updated       = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.answerText + " for question : " + self.question.questionText

class Score(models.Model):
    score                   = models.PositiveIntegerField(null = False, blank = False)
    timestamp               = models.DateTimeField(auto_now_add = True) 
    updated                 = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'Student with id {} scored {}'.format(self.id,self.score)