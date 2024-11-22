from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.
admin.site.site_header = "E-commerce"
admin.site.site_title = "Habitat Online"
admin.site.index_title = "Manageur"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added','disponibilite', )  
    search_fields = ('title', 'description',)
    list_editable = ('price','category','disponibilite',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays', 'total', 'file', 'date_commande',)



admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)