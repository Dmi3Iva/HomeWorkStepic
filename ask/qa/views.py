from django.http import HttpResponse, Http404
from django.shortcuts import render

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def home(request):
	Question.objects.new(request)

def popular(request):
	Question.objects.popular(request)

def question(request, pk):
	Question.objects.question(request, pk)
