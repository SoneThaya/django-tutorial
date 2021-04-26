from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

# Create your views here.
def first(request):
    books = Book.objects.all()
    
    return render(request, 'first_temp.html', {'books': books})



# class Another(View):
    
#     book = Book.objects.get(id=2)
#     output = f"We have {book.title} book with ID {book.id}.<br>"
    
#     #for book in books:
#     #    output += f"We have {book.title} book with ID {book.id} in DB.<br>"
    
#     def get(self, request):
#         return HttpResponse(self.output)
    

