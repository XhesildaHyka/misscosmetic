from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.home, name='home'),
    path('arrival/<int:id>/', views.arrival, name='arrivalpage'),
    path("details/<int:id>", views.details, name="detailspage"),
    path('marka/<int:marka_id>/', views.marka, name='marka'),
    path('makeup/<int:makeup_id>/', views.makeup, name='makeup'),
    path('skincare/<int:skincare_id>/', views.skincare, name='skincare'),
]