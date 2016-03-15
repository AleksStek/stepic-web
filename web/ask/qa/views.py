from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from models import Question, Answer
from functions import pagepag
from forms import AskForm, AnswerForm

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
def questempty(request):
	return HttpResponseRedirect('/question/1/')
def questpage(request, slug):
	question = get_object_or_404(Question, pk=slug)
	return render(request, 'quest.html',{
		'question': question,
		'answers': Answer.objects.filter(question=slug).order_by('-added_ad')[:],
		'newanswer': AnswerForm({'question': int(slug)}),
	},)

def askform(request):
	url = '/question/'
	if request.method == "POST":
		ask = AskForm(request.POST)
		if ask.is_valid():
			url = url + str( ask.save() ) + '/'
		return HttpResponseRedirect(url)
	else:
		ask = AskForm()
	return render(request, 'ask.html',{
		'ask': ask,
	},)

def newanswer(request):
	url = '/question/'
	if request.method == "POST":
		newanswer = AnswerForm(request.POST)
		if newanswer.is_valid():
			url = url + str(newanswer.save()) + '/'
	return HttpResponseRedirect(url) 
