from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView, DeleteView
from django.views.generic.base import TemplateResponseMixin

from .models import Question, Choice
from .mixins import RequireLoginMixin

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

def vote(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST.get['choice'])
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'polls?detail.html', {'question': question})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Class Based Views
class IndexView(RequireLoginMixin, ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class VoteView(View):
    def get_queryset(self, choice_id):
        return Choice.objects.get(pk=choice_id)

    def post(self, request, pk):
        question_id = pk
        choice_id = request.POST.get('choice', None)
        
        try:
            queryset = self.get_queryset(choice_id)
        except(KeyError, Choice.DoesNotExist):
            return redirect('polls:detail', pk=question_id)
        else:
            queryset.votes += 1
            queryset.save()
            return redirect('polls:results', pk=question_id)

class ResultsView(TemplateResponseMixin, View):

    def get_queryset(self, question_id):
        return Question.objects.get(pk=question_id)

    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        context = {'question': queryset}
        return render(request, 'polls/results.html', context)