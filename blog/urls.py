from django.urls import path
from . import views

app_name = 'blog'
urlpatterns =[
    # index
    path('', views.post_list, name='post_list'),

    # localhost/post/postID
    path('post/<int:pk>', views.post_detail, name='post_detail'),


    path('post/new/', views.post_new, name='post_new')

]
