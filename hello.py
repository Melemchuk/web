def wsgi_application(environ,start_response):
  body = [(i+"\n").encode('utf-8') for i in environ["QUERY_STRING"].split("&")]
  start_response("200 OK",[("Content_Type","text/plain")])
  return body
