from re import template
from urllib import response
import django
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Choise,Question

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model =Question
    template_name = 'polls/results.html'

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})


def index(request):
    #return HttpResponse("Primera pagina con django y polls")
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #template= loader.get_template('poll/index.html')
    #output=', '.join([q.question_text for q in latest_question_list])
    context ={
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

""" def detail(request, question_id):
    return HttpResponse(" you're looking at question %s. " %question_id) """

def results(request, question_id):
    
    question =get_object_or_404(Question, pk=question_id)
    return render(request , 'polls/results.html',{'question':question})

def vote (request, question_id):
    #return HttpResponse("you're voting on question %s. "%question_id)
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choise= question.choise_set.get(pk=request.POST['choise'])
    except(KeyError, Choise.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choise",
        })
    else:
        selected_choise.votes +=1
        selected_choise.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))





