from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book, Author, BookInstance, Collection, Magazine
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

@login_required
def index(request):
    books = Book.objects.all()
    magazines = Magazine.objects.all()
    
    context = {
        'books': books,
        'magazines':magazines,
    }
    return render(request, 'catalog_app/index.html', context)

def borrowing_a_book(request):
    pk = request.POST["pk"]
    book_instance = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            book_instance.borrower = request.user
            book_instance.due_back = datetime.date.today() + datetime.timedelta(weeks=3)
            book_instance.status = STATUS_ON_LOAN
            book_instance.save()
            return redirect('index')

    context = {
       'book_instance': book_instance,
    }

    return render(request, 'catalog_app/index.html', context)



class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog_app/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
