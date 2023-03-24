from django.shortcuts import render

def book_list (request):
    context = {'title': 'Page d\'accueil de PhilTub'}
    return render (request, 'booklist/book_list.html', context)

