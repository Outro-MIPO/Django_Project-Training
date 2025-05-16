from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import CommandeForm

from .models import Commande
from django.contrib.auth.decorators import login_required#Pour ne plus permettre de se connecter si on a pas de compte


@login_required(login_url='acces')
def liste_commande(request):
    return render(request,'commande/liste_commande.html')

@login_required(login_url='acces')
def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form=CommandeForm(request.POST)
        if form.is_valid():#Es ce que les donnees que nous avons mis a l'interieur du formulaire sont valides
            form.save()
            return redirect('/produit')#Use to redirect where we wana to go
        
    context={'form':form}#Poour pousser notre formulaire vers la page en question
    
    return render(request,'commande/ajouter_commande.html',context)
@login_required(login_url='acces')
def modifier_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():#Es ce que les donnees que nous avons mis a l'interieur du formulaire sont valides
            form.save()
            return redirect('/produit')#Use to redirect where we wana to go
        
    context={'form':form}#Poour pousser notre formulaire vers la page en question
    
    return render(request,'commande/ajouter_commande.html',context)

@login_required(login_url='acces')
def supprimer_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    
    if request.method=='POST':
        commande.delete()
        return redirect('/produit')
    context={'item':commande}#item pour ne pas du tout avoir de confusion avec context au dessus
        
    return render(request,'commande/supprimer_commande.html',context)