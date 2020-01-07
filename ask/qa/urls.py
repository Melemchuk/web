from qa.views import test
from django.conf.urls import url#,patterns
urlpatterns = [
    url(r'^',test,name='test')
]
