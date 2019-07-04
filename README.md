# scrapy-intermarche
Extraire le contenu d'un site web e-commerce (magasin, catégorie, produit et prix, ...)
Pour le site Intermarché.
Il n’y a pas qu’un seul crawler pour tout le site mais plusieurs parties qui extraient différents
éléments.

=> Crawler 1
Récupération de la liste des magasins avec le maximum d’information.
- un identifiant unique (obligatoire)
- nom
- adresse
- numéro téléphone
- mail
- URL
- ville
- code postal
- latitude
- longitude

=> Crawler 2
Récupération de la liste des catégories pour un magasin.
Il faut utiliser le fichier précédent si nécessaire (besoin de l’id / url du magasin ?)
Il faut se connecter au magasin visé avant de pouvoir en extraire les informations.
- un identifiant unique (obligatoire)
- identifiant de la catégorie parente (obligatoire)
- URL
- level
- feuille (True/False) (la catégorie est-elle une feuille de l’arbre ?)

=> Crawler 3
Récupération de la liste des produits pour un seul magasin.
De même, Il faut utiliser le fichier précédent. Idéalement, on ne crawl que les catégories les
plus basses (les feuilles).
Il faut se connecter au magasin visé avant de pouvoir en extraire les informations.
- identifiant unique (obligatoire)
- nom
- prix
- prix barré (ancien prix)
- promo (libellé)

=> Crawler 4
Récupération des fiches produits pour un seul magasin
De même, Il faut utiliser le fichier précédent et se baser sur les URL de chaque produits.
Il faut se connecter au magasin visé avant de pouvoir en extraire les informations.
- identifiant unique (obligatoire)
- nom
- marque
- URL
- URL de l’image
- quantité

-----------------------------------------------------------------
ETAPES POUR TESTER LE SCRAPING :
1 - Configuration du système
- Vous devez avoir minimum python 3.5 installé sur votre machine
- Vous créez votre virtualenv, Sinon installer : $ virtualenv --python=python3 venv
- Installer scrapy : $ pip install scrapy
- Copier le projet 'intermarche'

2 - Commencez le test avec en lançant une à une les commandes suivantes et récuperer les fichiers jsons:
- scrapy crawl spider_magasin -o magasins.json
- scrapy crawl spider_category -o categories.json
- scrapy crawl spider_product -o produits.json
- scrapy crawl spider_product_info -o produits_fiches.json
