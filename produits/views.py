from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Facture, FactureLigne
from .forms import ProduitForm


def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/ajouter_produit.html', {'form': form})


def modifier_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/modifier_produit.html', {'form': form})


def supprimer_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'produits/supprimer_produit.html', {'produit': produit})


def creer_facture(request):
    produits = Produit.objects.all()
    if request.method == 'POST':
        ids_selectionnes = request.POST.getlist('produits')
        if ids_selectionnes:
            facture = Facture.objects.create()
            for pid in ids_selectionnes:
                produit = Produit.objects.get(id=pid)
                FactureLigne.objects.create(
                    facture=facture,
                    nom_produit=produit.nom,
                    prix_unitaire=produit.prix,
                    date_peremption=produit.date_peremption
                )
            return redirect('detail_facture', id=facture.id)
    return render(request, 'produits/creer_facture.html', {'produits': produits})


def detail_facture(request, id):
    facture = get_object_or_404(Facture, id=id)
    lignes = facture.lignes.all()
    total = sum(l.prix_unitaire for l in lignes)
    return render(request, 'produits/detail_facture.html', {
        'facture': facture,
        'lignes': lignes,
        'total': total
    })


def liste_factures(request):
    factures = Facture.objects.all().order_by('-date_creation')
    return render(request, 'produits/liste_factures.html', {'factures': factures})
