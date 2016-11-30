from django.db import models

class Question(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  added_at = models.DateField(true)
  rating = models.IntegerField()
  # author = django.contrib.auth.models.User
  # likes = [django.contrib.auth.models.User]

  def __unicode__(self):
    return self.title

  class Meta:
    pass

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField(true)
  # question = models.ForeignKey(Question)
  # author = django.contrib.auth.models.User

  def __unicode__(self):
    return 'Answer [id={}]'.format(self.pk)

  class Meta:
    pass

class QuestionManager(models.Manager):
  def new(self):
    return None

  def popular(self):
    return None
