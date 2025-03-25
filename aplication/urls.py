from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.home, name='home'),
    path("arrival/<int:id>", views.arrival, name="arrivalpage"),
    path("terms/", views.terms, name="terms"),
    # path("bestseller/<int:id>", views.bestseller, name="bestseller"),
    path("collection/<int:id>", views.collection, name="collection"),
    path("carousel_images/", views.carousel_images, name="carousel_images"),
    path("detail/<int:id>", views.detail, name="detailpage"),
    path('marka/<int:marka_id>/', views.marka, name='marka'),
    path('makeup/<int:makeup_id>/', views.makeup, name='makeup'),
    path('skincare/<int:skincare_id>/', views.skincare, name='skincare'),
    path('accessor/<int:accessor_id>/', views.accessor, name='accessor'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('offer/<int:id>', views.offer, name='offer'),
    path('search/', views.search, name='search'),
    path('video/', views.video, name='video'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('remove_item/<int:pk>/', views.remove_item, name='remove_item'),
    path('increase_item/<int:pk>/', views.increase_item, name='increase_item'),
    path('decrease_item/<int:pk>/', views.decrease_item, name='decrease_item'),
]