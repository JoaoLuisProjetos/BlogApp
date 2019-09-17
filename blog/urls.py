from django.urls import path
from . import views

app_name = 'blog'
urlpatterns =[
    # index
    path('', views.post_list, name='post_list'),

    path('drafts/', views.post_drafts, name='post_drafts'),
    # localhost/post/postID
    path('post/<int:pk>', views.post_detail, name='post_detail'),

    path('post/new/', views.post_new, name='post_new'),

    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
]
