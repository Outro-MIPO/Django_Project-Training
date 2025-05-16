from django.db import models

# Create your models here.


class Tag(models.Model):
     nom=models.CharField(max_length=200, null=True)
     
     def __str__(self):#Pour afficher only , le nom du client 
        return self.nom
    


class Produit(models.Model):#Pour prendre les caracteristique du model de django
    #la partie Id n'est pas definie , car elle est definit avec django par defaut
    
    nom=models.CharField(max_length=200, null=True)#nulll=True , valeur par defaut
    prix=models.FloatField(null=True)
    
    tag=models.ManyToManyField(Tag)
    
    
    def __str__(self):#Pour afficher only , le nom du client 
        return self.nom
