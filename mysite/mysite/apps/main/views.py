from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import LatestNewsModel, Comment
from django.http import Http404, HttpResponseRedirect


def index(request):
    news = LatestNewsModel.objects.all()
    context = {'news': news}
    return render(request, 'main/list.html', context)


def detail(request, new_id):
    try:
        new = LatestNewsModel.objects.get(id=new_id)
    except:
        raise Http404('Страница не найдена')

    latest_comment_list = new.comment_set.order_by('-id')[:10]

    context = {'new': new, 'latest_comment_list': latest_comment_list}
    return render(request, 'main/detail.html', context)


def leave_comment(request, new_id):
    try:
        new = LatestNewsModel.objects.get(id=new_id)
    except:
        raise Http404('Страница не найдена')

    new.comment_set.create(name=request.POST['name'], text=request.POST['text'])
    return HttpResponseRedirect(reverse('main:detail', args=(new_id,)))

