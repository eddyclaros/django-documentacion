from re import template
from urllib import response
import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
# Create your views here.
def index(request):
    #return HttpResponse("Primera pagina con django y polls")
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=', '.join([q.question_text for q in latest_question_list])
    context ={
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    return HttpResponse(" you're looking at question %s. " %question_id)

def results(request, question_id):
    response="you're looking at the results or question %s."
    return HttpResponse(response % question_id)

def vote (request, question_id):
    return HttpResponse("you're voting on question %s. "%question_id)





