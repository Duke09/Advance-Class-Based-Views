from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, DeleteView

from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request, 'polls/detail.html', {'question': question})

# Class Based Views
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
