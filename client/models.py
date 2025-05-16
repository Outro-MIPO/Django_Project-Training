from django.db import models

# Create your models here.

#Mettre toujours la premiere lettre en majuscule
class Client(models.Model):
    nom=models.CharField(max_length=200,null=True)
    telephone= models.CharField(max_length=200,null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)  #Datetime cela veux dire qu'on rajoute l'heure , # auto_now_add est un champ qui genere automatiquement la date
    
    def __str__(self):#Pour afficher only , le nom du client 
        return self.nom