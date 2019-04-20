def wsgi_application(environ,satart_response):
  body = [bytes(i+"\n","ascii") for i in environ["QUERY_STRING"].split("&")]
  satart_response = ("200 OK",[("Content_type","text/plain")])
  return body
