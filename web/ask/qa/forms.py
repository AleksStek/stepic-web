# coding: utf-8

from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	author = forms.CharField(label='Ваше Имя', max_length=255)
	title = forms.CharField(label='Заголовок вопроса', max_length=255)
	text = forms.CharField(label='Текст вопроса', widget=forms.Textarea)
	
	def save(self):
		quest = Question(**self.cleaned_data)
		quest.save()
		return quest.pk

class AnswerForm(forms.Form):
	author = forms.CharField(label='Ваше Имя', max_length=255)
	text = forms.CharField(label='Текст ответа', widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)

	def save(self):
		newanswer = Answer(text=self.cleaned_data['text'], author=self.cleaned_data['author'])
		newanswer.question = Question.objects.get(pk=self.cleaned_data['question'])
		newanswer.save()
		return self.cleaned_data['question']
