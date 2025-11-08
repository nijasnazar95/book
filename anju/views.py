from django.shortcuts import render,redirect,get_object_or_404
from .models import Book , Cart
from .forms import AddForm, RegestrtionForm , LoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

from django.conf import settings
import stripe
from django.urls import reverse 

stripe.api_key=settings.STRIPE_SECRET_KEY

# from django.http import HttpResponse
# # Create your views here.
# def home(request):
#     return HttpResponse("Homepage")
# def about(request):
#     return HttpResponse("Aboutuss")
# def audio(request):
#     return HttpResponse("musiccc")


def home(request):
    return render(request,"home.html")

@login_required
def index(request):
    return render(request,"index.html")

def view_book(request):
    books=Book.objects.all()
    return render (request,'books.html',{'page':books})

@login_required
def AddBook(request):
    form=AddForm (request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lines')
    return render(request,'line.html',{'forms':form})

@login_required
def update_book(request,id):
    book=Book.objects.get(id=id)
    form=AddForm(request.POST or None,request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('lines')
    return render(request,'update.html',{'forms':form})

@login_required
def delete_book(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        book.delete()
        return redirect('lines')
    return render(request,'confirmdlt.html',{'book':book})
    
def register_book(request):
    reg=RegestrtionForm(request.POST or None)
    if request.method=='POST' and reg.is_valid():
        reg.save() 
        return redirect('lines')
    return render(request,'registration.html',{'reg':reg})

def login_user(request):
    form=LoginForm(request,data=request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.get_user()
        login(request,user)
        return redirect('lines')
    return render(request,'login.html',{'abc':form})

def logout_user(request):
    logout(request)
    return redirect('loginpage')

def add_to_cart(request,book_id):
    book=Book.objects.get(id=book_id)
    cart_item, created = Cart.objects.get_or_create(book=book, user=request.user)
    if not created:
        cart_item.quantity +=1
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart_items=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cart_items:
        total_price += item.book.price * item.quantity
    return render (request, 'view_cart.html', {'cart_items':cart_items,'total_price':total_price})

def remove_from_cart(request,book_id):
    book=Book.objects.get(id=book_id)
    cart_item=Cart.objects.get(book=book,user=request.user)
    if cart_item.quantity >1:
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')

def buy_now(request, book_id):
    cart_items= Cart.objects.filter(user=request.user,book_id=book_id)
    if not cart_items.exists():
        return redirect('view_cart')
    book=get_object_or_404(Book,id=book_id)

    total_quantity= sum(item.quantity for item in cart_items)
    session=stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data':{
                    'currency':'inr',
                    'product_data':{
                        'name':book.name,
                    },
                    'unit_amount': int(float(book.price)*100),

                },
                'quantity':total_quantity
            }
        ],
        mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel')),

    )
    return redirect(session.url)

def payment_success(request):
    return render(request,'success.html')
def payment_cancel(request):
    return render(request,'cancel.html')
