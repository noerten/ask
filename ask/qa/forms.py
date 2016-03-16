
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
   

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question



class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

#    def save(self):
#        answer = Answer(**self.cleaned_data)
#        answer.save()
#        return answer

    def save(self):
        self.cleaned_data['question'] = Question(self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        answer.save()
        return answer

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user
