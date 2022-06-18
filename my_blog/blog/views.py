from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.

def main_page(request):
    return HttpResponse(render_to_string('blog/index.html'))


def posts(request):
    # return HttpResponse('Все посты блога')
    return render(request, 'blog/list_detail.html')


def name_post(request, post_name):
    data = {
        'post_name': post_name,
    }
    return render(request, 'blog/detail_by_name.html', context=data)


def number_post(request, post_number):
    data = {
        'post_number': post_number,
    }
    return render(request, 'blog/detail_by_number.html', context=data)
