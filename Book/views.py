from django.shortcuts import render, redirect
from Book.models import Book
from django.http import HttpResponse
import logging
logger = logging.getLogger('first')

# Create your views here.
def homepage(request):
    logger.info("In homepage View")
    all_book = Book.active_objects.all()
    logger.info(all_book)     
    return render(request,template_name='home.html',context={"books": all_book})

def save_book(request):
    logger.info(request.POST)
    b_name = request.POST.get("name")
    b_author = request.POST.get("author")
    b_price = request.POST.get("price")
    b_qty = request.POST.get("qty")
    b_pub = request.POST.get("pub")
    if b_pub == "on":
        flag = True
    else:
        flag = False
    
    if request.POST.get('id'):
        try:
            book_obj = Book.objects.get(id=request.POST.get('id'))
        except Exception as msg:
            logger.error(f"{msg} -- in exception")
        book_obj.name = b_name
        book_obj.author = b_author
        book_obj.qty = b_qty
        book_obj.price = b_price
        book_obj.is_publish = flag
        book_obj.save()
        return redirect('welcome')

    else:  
        b =Book(name=b_name, author=b_author, qty=b_qty, price=b_price, is_publish=flag)
        b.save()
        return redirect('welcome')



def edit(request,id):
    try: 
        book_obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        msg = f"No Such Book Exist"
        return HttpResponse(msg)

    all_book = Book.active_objects.all()
    return render(request, template_name='home.html', context={'book':book_obj, 'books':all_book})

def delete(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted='Y'
    book_obj.save()
    return redirect('welcome')

def show_deleted(request):
    all_deleted_books = Book.inactive_objects.all()
    return render(request,template_name='home.html',context={'books': all_deleted_books})

def hard_delete(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.delete()
    return redirect('welcome')

def restore(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted='N'
    book_obj.save()
    return redirect('welcome')
   
def delete_all(request):
    book_obj = Book.objects.all()
    for i in range(len(book_obj)):
        book_obj[i].is_deleted ='Y'
        book_obj[i].delete()
    return redirect('welcome')

def restore_all(request):
    book_obj = Book.objects.all()
    for i in range(len(book_obj)):
        book_obj[i].is_deleted='N'
        book_obj[i].save()
    return redirect('welcome')