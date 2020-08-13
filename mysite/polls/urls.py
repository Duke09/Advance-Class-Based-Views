from django.urls import path
from django.conf.urls import url

from .views import index, detail, IndexView, DetailView, DeleteView

app_name = 'polls'

urlpatterns = [
    # path('', index, name='index'),
    # path('polls/<int:question_id>/', detail, name='detail'),
    path('polls/', IndexView.as_view(), name='index'),
    path('polls/<int:pk>/', DetailView.as_view(), name='detail'),
    
    # using regular expression
    url(r'^$', IndexView.as_view(), name='polls_index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='polls_detail'),
]