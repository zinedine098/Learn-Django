from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.postDetail, name='post-detail'),
    path('create/', views.createPost, name='create-post'),
]
