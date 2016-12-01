from django.db import models
from django.contrib import auth

class Question(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  added_at = models.DateField(auto_now_add=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
  likes = models.ManyToManyField(auth.models.User, related_name='likes_by')
  objects = QuestionManager()

  def __unicode__(self):
    return self.title

  class Meta:
    pass

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField(auto_now_add=True)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  author = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)

  def __unicode__(self):
    return 'Answer [id={}]'.format(self.pk)

  class Meta:
    pass

class QuestionManager(models.Manager):
  def new(self):
    return Question.objects.order_by('-added_at')

  def popular(self):
    return Question.objects.order_by('-rating')
