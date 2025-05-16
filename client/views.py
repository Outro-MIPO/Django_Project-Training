
from django.shortcuts import render
from django.http import HttpResponse

from .models import Client
# Create your views here.
from django.contrib.auth.decorators import login_required#Pour ne plus permettre de se connecter si on a pas de compte


@login_required(login_url='acces')
def liste_client(request,pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total=commande.count()
    context={'client':client,'commande':commande,'commande_total':commande_total}
    return render(request,'client/liste_client.html',context)