from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from .models import Question, Answer
from django.views.decorators.http import require_GET

@require_GET
def main_page(request):
    questions = Question.objects.order_by('added_at')
    paginator, page = paginate(request, questions)
    return render(request, 'questions/some_page.html', {
        'puestions': page.object_list,
        'paginator': paginator, 'page': page,
        })
@require_GET
def popular(request):
    questions = Question.objects.filter.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1) #1 is default param if page isnt found
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page
    return render(request, 'questions/some_page.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
        })

@require_GET
def questions(request, qu_id):
    question = get_object_or_404(Question, pk=qu_id)
    answers = Answer.objects.filter(question_id__exact = int(qu_id))
    return render(request, 'questions/question.html',
                  {'title': question.title, 'text': question.text,
                   'answers': answers})#answer.text(question=question)})

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
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
