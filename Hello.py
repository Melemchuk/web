def wsgi_application(environ,satart_response):
  body = [bytes(i+"\n","ascii") for i in environ["QUERY_STRING"].split("&")]
  return body
