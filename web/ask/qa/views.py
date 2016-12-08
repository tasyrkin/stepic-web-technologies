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


def handle_request(request, page_number, base_url, query_set):
  paginator_util = models.PaginatorUtil(base_url, query_set)
  page = paginator_util.get_page(page_number)
  return render(request, 'paginated_question_list.html', {
    'page': page,
    'paginator': paginator_util.get_paginator(),
  })


def new(request, *args, **kwargs):
  page_number = __get_page_number_safely(request)
  base_url = '{}?page='.format(reverse(ask.urls_constants.NEW_URL_NAME))
  query_set = models.Question.objects.new()
  return handle_request(request, page_number, base_url, query_set)


def popular(request, *args, **kwargs):
  page_number = __get_page_number_safely(request)
  base_url = '{}?page='.format(reverse(ask.urls_constants.POPULAR_URL_NAME))
  query_set = models.Question.objects.popular()
  return handle_request(request, page_number, base_url, query_set)


@require_GET
def question_details(request, question_id):
  question = get_object_or_404(models.Question, pk=question_id)
  answers = models.Answer.objects.filter(question_id=question_id)
  return render(request, 'question_details.html', {
    'question': question,
    'answers': answers
  })
