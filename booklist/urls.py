from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('<int:post_id>/', views.detail, name='detail'),
    path('', views.book_list, name='book_list'), #differentiate booklist the app and book_list the view
]
