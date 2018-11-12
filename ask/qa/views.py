from django.http import HttpResponse, Http404
from django.shortcuts import render

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def home(request):
	Question.objects.new()

def popular(request):
	Question.objects.popular()

def question(request, point):
	Question.objects.question()
