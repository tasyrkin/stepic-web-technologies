import ask.urls_constants
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

  return page_number if page_number >= 1 else 1


def new(request, *args, **kwargs):
  page_number = __get_page_number_safely(request)
  baseurl = '{}?page='.format(reverse(ask.urls_constants.NEW_URL_NAME))

  paginator_util = models.QuestionPaginatorUtil(baseurl)
  page = paginator_util.get_page(page_number)

  return render(request, 'new_list.html', {
    'page': page,
    'paginator': paginator_util.get_paginator(),
  })

@require_GET
def question_details(request, question_id):
  question = get_object_or_404(models.Question, pk=question_id)
  answers = models.Answer.objects.filter(question_id=question_id)
  return render(request, 'question_details.html', {
    'question': question,
    'answers': answers
  })
