from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm#Importation du formulaire de creation utilisateur
from django.contrib.auth import authenticate, login,logout
from .forms import CreeUtilisateur
from django.contrib import messages
# Create your views here.

def inscriptionPage(request):
    
    form=CreeUtilisateur()
    
    if request.method == 'POST':
        form = CreeUtilisateur(request.POST)#Formulaire deja preetablie 
        
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte créé avec success pour '+user)#Pour recevoir le message de la creation du compte
            return redirect('acces')
            
    context={'form':form}
    
    return render(request,'compte/inscription.html',context)

def accesPage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            
            return redirect('accueil')
        else:
            messages.info(request,"il y a une erreur dans le nom d'utilisateur et/ ou mot de passe")
    
    return render(request,'compte/acces.html',context)


def logoutUser(request):
    logout(request)
    return redirect('acces')
