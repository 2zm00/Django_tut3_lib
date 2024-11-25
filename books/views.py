from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from books.models import Book, Review
# Create your views here.



class IndexView(generic.ListView):
	model = Book
	template_name = 'books/index.html'
	context_object_name = 'book_list'
	def get_queryset(self):
		return Book.objects.order_by("-pub_date")[:]





class DetailView(generic.DetailView):
	model = Book
	template_name = 'books/detail.html'

class CreateView(generic.CreateView):
	model = Book
	fields = ['title', 'author']
	template_name ='books/create.html'
	success_url = reverse_lazy('books:index')

class DeleteView(generic.DeleteView):
	model = Book
	template_name ='books/delete.html'
	context_object_name = 'book'
	success_url = reverse_lazy('books:index')

class ReviewCreateView(generic.CreateView):
	model = Review
	template_name='books/create_review.html'
	fields = ['review_text', 'book']
	def get_success_url(self) -> str:
		return reverse_lazy('books:detail',args=(self.object.book.id,))
	
class ReviewDeleteView(generic.DeleteView):
    model = Review
    template_name = 'books/delete_review.html'
    pk_url_kwarg = 'review_pk'
    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs={'pk': self.object.book.id,})



