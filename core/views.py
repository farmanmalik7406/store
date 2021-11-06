from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from core.models import Cart, Product
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authlogin


# Create your views here.
def home(request):
    productsSet = Product.objects.all()
    context = {'products' : productsSet}
    
    return render(request,'index.html',context)

def product_card(request):
    return HttpResponse("this is card")


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def registeruser(request):
    if request.method == 'POST':
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # validation
        if pass1 != pass2:
            return redirect('register')


        # creating user
        myuser = User.objects.create_user(email,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        

    else:
        return HttpResponse("not found")


def handlelogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        authlogin(request, user)
        # Redirect to a success page.
        return redirect('home')
    else:
        # Return an 'invalid login' error message
        return redirect('login')

def handlelogout(request):
    logout(request)
    return redirect('home')

def AddToCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = request.POST['product_id']
            product = Product.objects.get(id=product_id)
            quantity = int(request.POST['product_qty'])
            if Cart.objects.filter(product=product):
                total = product.price * quantity
                cart = Cart.objects.get(product=product)
                cart.quantity = quantity
                cart.total = total
                cart.save()
            else:
                total = product.price * quantity
                cart = Cart(user=request.user,product=product,quantity=quantity,total=total)
                cart.save()
            productsSet = Product.objects.all()
            context = {'products' : productsSet,'message':'added to cart'}
            return render(request,'index.html',context)
            
def Checkout(request):
    if request.user.is_authenticated:
        return render(request,'checkout.html')
    else:
        return redirect(home)