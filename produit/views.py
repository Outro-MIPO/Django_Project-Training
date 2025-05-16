from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from commande.models import Commande# partie fornd end c'est a dire ce que l'utilisateur verra
from client.models import Client
from django.contrib.auth.decorators import login_required#Pour ne plus permettre de se connecter si on a pas de compte


#Ramener , les elements dans la commande et client , pour afficher les elements dans la vue
@login_required(login_url='acces')#La personne qui nest pas authentifier est directement diriger vers la page acces
def home(request):
    
    commandes = Commande.objects.all()#Requette pour faire appel a toute les commandes
    clients= Client.objects.all()
    context={'commandes':commandes , 'clients':clients}#on met nos elements dans un dico
    return render(request,'produit/accueil.html',context)