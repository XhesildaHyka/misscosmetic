from django.shortcuts import render
from .models import *  # Make sure to import the models you need

def home(request):
    carousel_images = CarouselImage.objects.all()  
    detailItem = Product.objects.all()
    arrivals = Arrival.objects.all()  
    categories = Marka.objects.all()
    cat = Makeup.objects.all()
    cate = Skincare.objects.all()
    context = {
        'carousel_images': carousel_images,
        'arrivals': arrivals,  # Updated variable name
        'detailItem': detailItem,
        'range_5': range(1, 6),
        'categories': categories,
        'cat': cat,
        'cate': cate
    }
    return render(request, 'home.html', context)

def arrival(request, id):
    arrival= Arrival.objects.get(pk=id)  # Renamed for clarity
    new = Product.objects.filter(arrival=arrival)
    context = {"arrival": arrival, "new": new}
    return render(request, 'arrival.html', context)

def details(request, id):
    detail_item = Product.objects.get(pk=id)  # Renamed for consistency
    context = {"detailItem": detail_item}
    return render(request, 'detail.html', context)

def marka(request, marka_id):
    marka = Marka.objects.get(id=marka_id)  
    markat = Product.objects.filter(marka=marka)
    return render(request, 'marka.html', {'markat': markat})

def makeup(request, makeup_id):
    makeup = Makeup.objects.get(id=makeup_id)  # Get the makeup category
    make = Product.objects.filter(makeup=makeup)  # Get the products in that category
    return render(request, 'makeup.html', {'make': make, 'makeup': makeup})


def skincare(request, skincare_id):
    skincare = Skincare.objects.get(id=skincare_id)
    skin = Product.objects.filter(skincare=skincare)
    return render(request, 'skincare.html', {'skin': skin, 'skincare': skincare})
