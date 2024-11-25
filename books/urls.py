from django.contrib import admin
from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/create/', views.ReviewCreateView.as_view(), name='create_review'),
    path('<int:book_pk>/delete/<int:review_pk>', views.ReviewDeleteView.as_view(), name='delete_review'),
]