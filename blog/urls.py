from django.urls import path
from . import views
from django.contrib.auth.views import LoginView as auth_views

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

    # localhost:8080/account/login/
    path('login/', auth_views.as_view(template_name="registration/login.html"), name='login'),

    path('logout/', auth_views.as_view(template_name="registration/login.html"), name='logout'),
]
