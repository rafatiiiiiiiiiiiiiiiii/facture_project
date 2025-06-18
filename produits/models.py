from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom

class Facture(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(ligne.prix_unitaire for ligne in self.lignes.all())

    def nb_produits(self):
        return self.lignes.count()

    def __str__(self):
        return f"Facture #{self.id} - {self.date_creation.strftime('%Y-%m-%d')}"

class FactureLigne(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    nom_produit = models.CharField(max_length=100)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return f"{self.nom_produit} – {self.prix_unitaire} €"
