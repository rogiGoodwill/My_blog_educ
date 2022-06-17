from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('posts', views.posts),
    path('posts/<int:number_post>', views.number_post),
    path('posts/<str:name_post>', views.name_post),
]