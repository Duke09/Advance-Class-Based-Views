from django.urls import path
from django.conf.urls import url

from .views import ResultsView, SwitchBoardView, VoteView, index, detail, IndexView, DetailView, DeleteView

app_name = 'polls'

urlpatterns = [
    # path('', index, name='index'),
    # path('polls/<int:question_id>/', detail, name='detail'),
    path('polls/', IndexView.as_view(), name='index'),
    path('polls/<int:pk>/', DetailView.as_view(), name='detail'),
    path('polls/vote/<int:pk>/', VoteView.as_view(), name='vote'),
    path('polls/results/<int:pk>/', ResultsView.as_view(), name='results'),
    path('polls/<int:pk>/vote/', SwitchBoardView.as_view(), name='switchboard'),
    # using regular expression
    url(r'^$', IndexView.as_view(), name='polls_index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='polls_detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteView.as_view(), name='polls_delete'),
    url(r'^(?P<pk>[0-9]+)/vote/$', SwitchBoardView.as_view(), name='switchboard_view'),
]