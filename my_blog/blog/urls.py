from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('posts', views.posts),
    path('posts/<int:post_number>', views.number_post),
    path('posts/<str:post_name>', views.name_post),
]