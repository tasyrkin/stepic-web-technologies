
def wsgi_app(environ, start_response):
  qstring = environ['QUERY_STRING']
  start_response('200 OK', [('Content-Type', 'text/plain')])
  return '' if qstring is None qstring.replace('&', '\n')
