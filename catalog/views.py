from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

def index(request):

    # Generate some high-level counts
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_authors = Author.objects.count()

    # Available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list' # your own name for the template
    queryset = Book.objects.filter(title__icontains='war')[:5]
    template_name = 'books/book_list.html'

class BookDetailView(generic.ListView):
    model = Book