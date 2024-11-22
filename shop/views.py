from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product, Commande
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        file = request.FILES.get('file')
        com = Commande(items=items,total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode, file=file)
        com.save()
        return redirect('confirmation')

    return render(request, 'shop/checkout.html')

def acceuil(request):
    return render(request, 'shop/acceuil.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
        email = item.email
        address = item.address
        ville = item.ville
        pays = item.pays
        zipcode = item.zipcode
        items = item.items    
        total = item.total
        date_commande =item.date_commande

    return render(request, 'shop/confirmation.html', {'name': nom, 'items':items,'email':email,'address':address,'ville':ville,'pays':pays,'zipcode':zipcode,'total':total,'date_commande':date_commande})
