from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book, Author, Collection, Magazine
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from datetime import date, timedelta
from django.contrib import messages

@login_required
def index(request):
    books = Book.objects.all()
    magazines = Magazine.objects.all()
    magazines_overdue = Magazine.objects.filter(borrowed = True, due_back__lte = date.today())
    books_overdue = Book.objects.filter(borrowed = True, due_back__lte = date.today())
    context = {
        'books': books,
        'magazines':magazines,
        'magazines_overdue': magazines_overdue,
        'books_overdue': books_overdue,
    }

    return render(request, 'catalog_app/index.html', context)

@login_required
def borrowing_a_book(request):
    pk = request.POST["pk"]
    books = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if Book.objects.filter(borrower=request.user, borrowed = True).count() < 10:
                books.borrower = request.user
                books.due_back = date.today() + timedelta(days=30)
                books.borrowed = True
                books.save()
                return redirect('index')
            else:
                messages.info(request, f'Sorry, you have borrowed too many books for this month')
                return redirect('index')

@login_required
def borrowed_books(request):
    books_borrowed = Book.objects.filter(borrower=request.user, borrowed = True)
    magazines_borrowed = Magazine.objects.filter(borrower=request.user, borrowed = True)
    context = {
    'books_borrowed': books_borrowed,
    'magazines_borrowed': magazines_borrowed
    }

    return render(request, 'catalog_app/borrowed.html', context)

@login_required
def return_book(request):
    pk = request.POST["pk"]
    if request.method == 'POST':
        if request.user.is_authenticated:
            book = get_object_or_404(Book, pk=pk)
            book.borrower = None
            book.due_back = None
            book.borrowed = False
            book.save()
            return redirect('borrowed')
        
    return render(request, 'catalog_app/borrowed.html', context)

@login_required
def return_magazine(request):
    pk = request.POST["pk"]
    if request.method == 'POST':
        if request.user.is_authenticated:
            magazine = get_object_or_404(Magazine, pk=pk)
            magazine.borrower = None
            magazine.due_back = None
            magazine.borrowed = False
            magazine.save()
            return redirect('borrowed')
        
    return render(request, 'catalog_app/borrowed.html', context)


@login_required
def borrowed_overdue(request):
    books_borrowed = Book.objects.filter(borrower=request.user, borrowed = True)
    magazines_borrowed = Magazine.objects.filter(borrower=request.user, borrowed = True)
    context = {
    'books_borrowed': books_borrowed,
    'magazines_borrowed': magazines_borrowed
    }

    return render(request, 'catalog_app/borrowed.html', context)

@login_required
def borrowing_a_magazine(request):
    pk = request.POST["pk"]
    magazines = get_object_or_404(Magazine, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if Magazine.objects.filter(borrower=request.user, borrowed = True).count() < 3:
                magazines.borrower = request.user
                magazines.due_back = date.today() + timedelta(days=7)
                magazines.borrowed = True
                magazines.borrowed_date = date.today()
                magazines.save()
                return redirect('index')
            else:
                messages.info(request, f'Sorry, you have borrowed too many magazines for this week')
                return redirect('index')


class BookListView(ListView):
    model = Book
    template_name = 'catalog_app/booklist.html'
    context_object_name = 'books'
    queryset = Book.objects.filter(borrowed = True)
    ordering = ['due_back']

class MagazineListView(ListView):
    model = Magazine
    template_name = 'catalog_app/magazinelist.html'
    context_object_name = 'magazines'
    queryset = Magazine.objects.filter(borrowed = True)
    ordering = ['due_back']