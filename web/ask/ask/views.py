
from django.http import HttpResponse 

def stub_ok(request, *args, **kwargs):
  return HttpResponse('OK')
