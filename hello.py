def wsgi_application(environ,start_response):
  body = [b(i+"\n") for i in environ["QUERY_STRING"].split("&")]
  start_response = ("200 OK",[("Content_type","text/plain")])
  return body
