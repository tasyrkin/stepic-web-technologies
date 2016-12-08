from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models


class QuestionManager(models.Manager):
  def new(self):
    return Question.objects.order_by('-added_at')

  def popular(self):
    return Question.objects.order_by('-rating')


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


class QuestionPaginatorUtil:
  ITEMS_PER_PAGE = 10

  def __init__(self, baseurl):
    self.paginator = self.__construct_paginator(baseurl)

  def __construct_paginator(self, baseurl):
    paginator = Paginator(Question.objects.new(), per_page=self.ITEMS_PER_PAGE)
    paginator.baseurl = baseurl
    return paginator

  def get_paginator(self):
    return self.paginator

  def __get_page_or_none(self, page_number):
    '''
    :param page_number:
    :return: page if it is possible, None if some exception has occurred
    '''
    try:
      return self.paginator.page(page_number)
    except:
      return None

  def get_page(self, page_number):
    '''
    Constructs page for the given page number
    :param page_number:
    :return: constructed page if it exists, None if no page exists
    '''
    try:
      page = self.paginator.page(page_number)
    except EmptyPage:
      page = self.__get_page_or_none(self.paginator.num_pages)
    except PageNotAnInteger:
      page = self.__get_page_or_none(1)
    return page
