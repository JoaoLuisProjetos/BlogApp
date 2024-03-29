from django.urls import path
from . import views

app_name = 'blog'
urlpatterns =[
    # index: localhost:8080
    path('', views.post_list, name='post_list'),

    # localhost:8080/drafts
    path('drafts/', views.post_drafts, name='post_drafts'),

    # localhost:8080/post/ID
    path('post/<int:pk>', views.post_detail, name='post_detail'),

    # localhost:8080/post/new/
    path('post/new/', views.post_new, name='post_new'),

    # localhost:8080/post/ID/edit/
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # localhost:8080/post/ID/publish/
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    path('post/<int:pk>/comment/', views.comment_to_a_post, name='comment_to_a_post'),

    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),

    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),

    path('signup/', views.signup, name='signup'),
]
