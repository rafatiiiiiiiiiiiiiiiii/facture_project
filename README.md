# 💼 Facture Project – Application de gestion de factures avec Django

Ce projet est une application web simple de gestion de produits et de factures, développée avec Django. Il permet d’ajouter, modifier, supprimer des produits, et de générer des factures associées tout en conservant un historique sécurisé.

## 🚀 Fonctionnalités principales

- 🔍 Liste des produits avec date de péremption et prix
- 🧾 Création et consultation de factures
- ❌ Suppression d’un produit **sans altérer les factures existantes**
- ✏️ Interface de modification des produits
- 💾 Interface CRUD simple et intuitive

## 📸 Aperçu

> Page d’accueil avec produits listés et actions  
> Page de facture avec détail des lignes de commande  

## 🛠️ Technologies utilisées

- Python 3.12
- Django
- HTML/CSS
- Bootstrap (à intégrer pour un style plus moderne)

## 🧰 Installation

```bash
git clone https://github.com/rafatiiiiiiiiiiiiiiiii/facture_project.git
cd facture_project
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
