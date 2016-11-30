from django.db import models

class Question(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  added_at = models.DateField(auto_now_add=True)
  rating = models.IntegerField()
  author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
  # likes = [django.contrib.auth.models.User]

  def __unicode__(self):
    return self.title

  class Meta:
    pass

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField(auto_now_add=True)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)

  def __unicode__(self):
    return 'Answer [id={}]'.format(self.pk)

  class Meta:
    pass

class QuestionManager(models.Manager):
  def new(self):
    return None

  def popular(self):
    return None
