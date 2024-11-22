from django.urls import path
from shop.views import index, detail, checkout, acceuil, confirmation

urlpatterns = [
    path('', index, name='home'),
    path( '<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('acceuil', acceuil, name= "acceuil"),
    path('confirmation', confirmation, name="confirmation"),
]

