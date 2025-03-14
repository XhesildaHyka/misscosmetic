from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.home, name='home'),
    path("arrival/<int:id>", views.arrival, name="arrivalpage"),
    path("carousel_images/", views.carousel_images, name="carousel_images"),
    path("detail/<int:id>", views.detail, name="detailpage"),
    path('marka/<int:marka_id>/', views.marka, name='marka'),
    path('makeup/<int:makeup_id>/', views.makeup, name='makeup'),
    path('skincare/<int:skincare_id>/', views.skincare, name='skincare'),
    path('accessor/<int:accessor_id>/', views.accessor, name='accessor'),
    path('contact/', views.contact, name='contact'),
    path('offer/<int:id>', views.offer, name='offer'),
    path('search/', views.search, name='search'),
    path('video/', views.video, name='video'),
]