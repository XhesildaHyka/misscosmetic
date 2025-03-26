from django.shortcuts import render
from .models import *  
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect

def home(request):
    carousel_images = CarouselImage.objects.all()  
    detailItem = Product.objects.all()
    arrivals = Arrival.objects.all() 
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    offer = Offer.objects.all()
    collection = Collection.objects.all()
    videos = Video.objects.all()
    bestseller = Product.objects.filter(is_bestseller=True)

   
   
    context = {
        'carousel_images': carousel_images,
        'arrivals': arrivals, 
        'collection': collection,
        'bestseller': bestseller,
        'detailItem': detailItem,
        'range_5': range(1, 6),
        'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'offer': offer,
        'videos': videos,
   
        

      
    }
    return render(request, 'home.html', context)

def carousel_images(request):
    carousel_images = CarouselImage.objects.get()
    return render(request, 'home.html', {'carousel_images': carousel_images})


def arrival(request, id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    arrivals = Arrival.objects.get(pk=id)  
    reja = Product.objects.filter(arrival_id=arrivals)
    arrival=Product.objects.filter(arrival_id=arrivals)
    paginator = Paginator(arrival, 8)  # Show 10 products per page

    # Get the page number from the query string (default to page 1)
    page_number = request.GET.get('page')
    
    # Get the page object based on the page number
    page_obj = paginator.get_page(page_number)

    context = {"arrivals": arrivals, "reja": reja,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'page_obj': page_obj,} 
    return render(request, 'arrival.html', context)



def collection(request, id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    collection = Collection.objects.get(pk=id)  
    koleksion = Product.objects.filter(collection_id=collection)
    paginator = Paginator(koleksion, 8)  # Show 10 products per page

    # Get the page number from the query string (default to page 1)
    page_number = request.GET.get('page')
    
    # Get the page object based on the page number
    page_obj = paginator.get_page(page_number)
    context = {"collection": collection, "koleksion": koleksion,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'page_obj':page_obj} 
    return render(request, 'collection.html', context)

def offer(request, id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    offer = Offer.objects.get(pk=id)  
    skonto = Product.objects.filter(offer_id=offer)
    paginator = Paginator(skonto, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"offer": offer, "skonto": skonto,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'page_obj':page_obj} 
    return render(request, 'offers.html', context)

def contact(request):   
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    if request.method == "POST":
       first_name= request.POST["emri"]
       last_name= request.POST["lastname"]
       email= request.POST["email"]
       message= request.POST["sms"]
       Contact(contact_name=first_name,contact_lastname=last_name,contact_email=email,contact_sms=message).save()
    context = {'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'contact.html', context)

def about(request):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    context = {'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'about.html', context)

def terms(request):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    context = {'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'terms.html', context)

def detail(request, id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()

    detailItem = Product.objects.get(pk=id)
    context = {"detailItem": detailItem,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'detail.html', context)


def marka(request, marka_id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    marka = Marka.objects.get(pk=marka_id)
    markat =Product.objects.filter(marka=marka)
    paginator = Paginator(markat, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"marka": marka, "markat": markat,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'page_obj':page_obj}
    return render(request, 'marka.html', context)

def makeup(request,makeup_id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    makeup = Makeup.objects.get(pk=makeup_id)  
    make = Product.objects.filter(makeup=makeup)
    paginator = Paginator(make, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"make": make, "makeup": makeup,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'page_obj': page_obj}
    return render(request, 'makeup.html', context)


def skincare(request, skincare_id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    skincare = Skincare.objects.get(pk=skincare_id)  
    skin = Product.objects.filter(skincare=skincare)
    paginator = Paginator(skin, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"skin": skin, "skincare": skincare,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'page_obj':page_obj}
    return render(request, 'skincare.html', context)

def accessor(request, accessor_id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    accessor = Accessor.objects.get(pk=accessor_id)  # Get the accessor category
    access = Product.objects.filter(accessor=accessor)
    paginator = Paginator(access, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"access": access, "accessor": accessor,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,
        'page_obj': page_obj}
    return render(request, 'accessor.html', context)


def search(request):
    search = request.GET.get("search")
    if search:
        posts = Product.objects.filter(
            Q(name__icontains=search) 
        )
    else:
        posts = Product.objects.all()
    return render(request, 'search.html', {"posts": posts})


def video(request):
    videos = Video.objects.get()
    return render(request, 'home.html', {'videos': videos})





@login_required

def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs.first()
        if order.orderitems.filter(item=item).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.orderitems.add(order_item)
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        message = f"'{item.name}' has been added to your cart."
        return JsonResponse({'message': message})
    else:
        messages.success(request, f"'{item.name}' has been added to your cart.")
        referer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referer)
    
def cart(request):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    carts = Cart.objects.filter(purchased=False)
    orders = Order.objects.filter(ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        context = {
           'categories': categories,
            'cat': cat,
            'cate': cate,
            'categ': categ,
            'carts': carts,
            'order': order
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('home')

@login_required
def remove_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.get(
                item=item, user=request.user, purchased=False
            )
            order.orderitems.remove(order_item)
            order_item.delete()
    return redirect('cart')


def increase_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(
                item=item, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('cart')

def decrease_item(request, pk):

    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(
                item=item, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect('cart')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('cart')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect if already logged in

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')  # Get intended destination
            messages.success(request, "You have been logged in successfully.")
            return redirect(next_url if next_url else '/')  # Redirect accordingly
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    request.session.flush()  # Clears session data
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')



@login_required
def cart(request):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    
    # Filter carts and orders by the logged-in user
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    
    if orders.exists():
        order = orders.first()
        context = {
            'categories': categories,
            'cat': cat,
            'cate': cate,
            'categ': categ,
            'carts': carts,
            'order': order,
            'is_cart_empty': not carts.exists()  # True if no items in cart
        }
        return render(request, 'cart.html', context)
    else:
        context = {
            'categories': categories,
            'cat': cat,
            'cate': cate,
            'categ': categ,
            'is_cart_empty': True  # Cart is empty if no active orders
        }
        return render(request, 'cart.html', context)