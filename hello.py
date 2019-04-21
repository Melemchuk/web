def wsgi_application(environ,satart_response):
  body = [(i+"\n").encode('utf-8') for i in environ["QUERY_STRING"].split("&")]
  satart_response = ("200 OK",[("Content_type","text/plain")])
  return body
