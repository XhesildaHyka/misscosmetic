from django.shortcuts import render
from .models import *  # Make sure to import the models you need

def home(request):
    carousel_images = CarouselImage.objects.all()  
    detailItem = Product.objects.all()
    arrivals = Arrival.objects.all  
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    offer = Offer.objects.all()
    videos = Video.objects.all()
    
    context = {
        'carousel_images': carousel_images,
        'arrivals': arrivals,  
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
    context = {"arrivals": arrivals, "reja": reja,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,} 
    return render(request, 'arrival.html', context)

def offer(request, id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()
    offer = Offer.objects.get(pk=id)  
    skonto = Product.objects.filter(offer_id=offer)
    context = {"offer": offer, "skonto": skonto,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,} 
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


def detail(request, id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()

    detail_item = Product.objects.get(pk=id)  
    context = {"detailItem": detail_item,'categories': categories,
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
    context = {"marka": marka, "markat": markat,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'marka.html', context)

def makeup(request,makeup_id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()

    makeup = Makeup.objects.get(pk=makeup_id)  # Get the makeup category
    make = Product.objects.filter(makeup=makeup)
    context = {"make": make, "makeup": makeup,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'makeup.html', context)


def skincare(request, skincare_id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()

    skincare = Skincare.objects.get(pk=skincare_id)  # Get the skincare category
    skin = Product.objects.filter(skincare=skincare)
    context = {"skin": skin, "skincare": skincare,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'skincare.html', context)

def accessor(request, accessor_id):
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    categ = Accessor.objects.all()

    accessor = Accessor.objects.get(pk=accessor_id)  # Get the accessor category
    access = Product.objects.filter(accessor=accessor)
    context = {"access": access, "accessor": accessor,'categories': categories,
        'cat': cat,
        'cate': cate,
        'categ': categ,}
    return render(request, 'accessor.html', context)



def search(request):
    search = request.GET.get("search")
    if search:
        posts = Product.objects.filter(product_title__icontains=search)
    else:
        posts = Product.objects.all()
    return render(request, 'search.html', {"posts": posts})

def video(request):
    videos = Video.objects.get()
    return render(request, 'home.html', {'videos': videos})