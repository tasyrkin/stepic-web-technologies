import ask.urls_constants
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa import models


def test(request, *args, **kwargs):
  return HttpResponse('OK')


def __get_page_number_safely(request):
  try:
    page_number = int(request.GET.get('page', 1))
  except:
    page_number = 1
  return page_number


def new(request, *args, **kwargs):
  page_number = __get_page_number_safely(request)
  paginator = __construct_paginator()

  page = paginator.page(page_number)

  return render(request, 'new_list.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
  })


def __construct_paginator():
  paginator = Paginator(models.Question.objects.new(), per_page=10)
  paginator.baseurl = '{}?page='.format(reverse(ask.urls_constants.NEW_URL_NAME))
  return paginator


@require_GET
def question_details(request, question_id):
  question = get_object_or_404(models.Question, pk=question_id)
  answers = models.Answer.objects.filter(question_id=question_id)
  return render(request, 'question_details.html', {
    'question': question,
    'answers': answers
  })
