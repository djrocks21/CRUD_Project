# from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book

# Create your views here.


from datetime import date

def homepage(request):
    if request.method == "POST":
        data = request.POST
        if data["ispub"] == "YES":
            Book.objects.create(name = data["nm"],
                qty = data["qty"],
                price = data["price"],
                is_published = True,
                published_date=date.today())
        elif data["ispub"] == "NO":
            Book.objects.create(name = data["nm"],
                qty = data["qty"],
                price = data["price"],
                is_published = False)
        return redirect("home")    
    else:
        return render(request, template_name="home.html")         
    
        

    # return HttpResponse("Hi Welcome to Home Page")



def get_books(request):
    books = Book.objects.all()
    return render(request, template_name="books.html", context={"all_books": books})


def delete_book(request, id):
    # print(id,"delete book id")
    Book.objects.get(id=id).delete() 
    return redirect("showbook")


def update_book(request, id):
    book_obj = Book.objects.get(id=id)
    return render(request, "home.html", context={"single_book": book_obj})












