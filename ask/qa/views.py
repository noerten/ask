from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm#, SignupForm, LoginForm
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.context_processors import csrf
#import django.middleware.csrf.CsrfViewMiddleware
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

from django.views.decorators.http import require_GET

@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def main_page(request):
    questions = Question.objects.order_by('-id')
    paginator, page = paginate(request, questions)
    return render(request, 'questions/some_page.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        })

@require_GET
def popular(request):
    questions = Question.objects.order_by('-rating')
    paginator, page = paginate(request, questions)
    return render(request, 'questions/some_page.html', {
        'questions': page.object_list,
        'paginator': paginator, 
        'page': page,
        })

@require_GET
def questions(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    form = AnswerForm(initial={'question': question.id})
    return render(request, 'questions/question.html', {
        "question": question,
        "answers": answers.all(),
        "form": form,
        "title": "Question detail"
    })


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 10:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

@csrf_protect
def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse('question', kwargs={'question_id': question.id}))

    else:
        form = AskForm()
    return render(request, 'questions/question_add.html', {
        'form': form
        })

@csrf_protect
def answer_add(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(reverse('question', kwargs={'question_id': answer.question.id}))
    else:
        form = AnswerForm()
  #  return render(request, 'questions/answer.html', {
  #      'form': form
  #      })

