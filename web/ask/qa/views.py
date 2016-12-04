from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse 

from qa import models

def test(request, *args, **kwargs):
  return HttpResponse('OK')

def new(request, *args, **kwargs):
  return HttpResponse('Got it')

@require_GET
def question_details(request, question_id):
  question = get_object_or_404(models.Question, pk=question_id)
  return render(request, 'question_details.html', {
    'question' : question
  })
