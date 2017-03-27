from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    # Generates counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    #Available Books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(
        request,
        'catalog/index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    context_objcet_name = "my_book_list"
    # queryset = Book.objects.filter(title__icontains='war')[:5]

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        context['some_data'] = 'This is just some dummy data'
        return context