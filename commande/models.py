from django.db import models
from client.models import Client# importation du models client de l'app commande
from produit.models import Produit

# Create your models here.


class Commande(models.Model):
    STATUS=(('en instance','en instance'),
            ('non livré','non livré'),
            ('livré','livré'))
    client=models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)#Relation 1 to many , on_delete lorsqu'on supprime , le model client qu'es ce qui arrivera a la commande, la disparition d'un client ne doit pas affecter celle dune commande
    produit = models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        self.client
    
    