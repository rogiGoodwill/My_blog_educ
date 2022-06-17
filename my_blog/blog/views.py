from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.

def main_page(request):
    return HttpResponse(render_to_string('blog/index.html'))


def posts(request):
    #return HttpResponse('Все посты блога')
    return render(request, 'blog/list_detail.html')


def name_post(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')


def number_post(request, number_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
