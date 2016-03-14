from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Question, Answer
from functions import pagepag

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def basetemp(request, url, order='-added_ad'):
	questions = Question.objects.all()
	questions = questions.order_by(order)
	[paginator,page] = pagepag(request, questions, url)
	return render(request, 'index.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	},)

def questpage(request, slug):
	question = get_object_or_404(Question, pk=slug)
	return render(request, 'quest.html',{
		'question': question,
		'answers': Answer.objects.filter(question=slug).order_by('-added_ad')[:]
	},)
