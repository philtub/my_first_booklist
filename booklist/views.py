from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book

def book_list (request):
    ######context = {'title': 'Page d\'accueil PhilTub'}
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    ######return render (request, 'booklist/book_list.html', context)
    return render (request, 'booklist/book_list.html', {'books':books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'booklist/book_detail.html', {'book': book})