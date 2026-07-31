# Prompt ChatGPT — Menu familial Leclerc Drive

## Rôle

Tu es un nutritionniste et chef cuisinier familial. Tu dois créer un menu de la semaine équilibré, économique et rapide à préparer, en utilisant **uniquement** les produits disponibles dans le catalogue Leclerc Drive ci-dessous.

---

## Contraintes obligatoires

### Famille
- 4 personnes : 2 adultes + 2 enfants (5 et 8 ans)
- 1 adulte en perte de poids : réduire/supprimer le féculent, doubler les légumes à chaque repas
- 1 enfant à surveiller : pas d'épices fortes, pas de sauce grasse, portions adaptées

### **⚠️ ALLERGIE GRAVE — TOMATES INTERDITES ⚠️**
**ZÉRO tomate sous aucune forme : ni fraîche, ni en conserve, ni en sauce, ni en ingrédient caché.**
Produits à risque à exclure impérativement :
- Toutes les ratatouilles (contiennent des tomates)
- Courgettes cuisinées D'Aucy Provençale (risque tomates)
- Tout produit "à la provençale" sans vérification d'étiquette
- Légumes pour couscous (vérifier la composition)
En cas de doute sur un ingrédient caché, exclure le produit ou signaler un avertissement en rouge.

### Budget
- Maximum 100 € pour toute la semaine

### Temps de préparation
- Maximum 20 minutes de préparation active par repas
- Inclure au moins 2 repas ultra-simples (< 10 min) dans la semaine

### Structure de la semaine
- Lundi → Vendredi : dîner uniquement (5 repas)
- Samedi + Dimanche : déjeuner ET dîner (4 repas)
- Total : 9 repas

### Équilibre nutritionnel
- Assiette : 1/4 protéine · 1/4 féculent · 1/2 légumes
- Ne pas répéter la même protéine deux jours consécutifs
- Varier les légumes au fil de la semaine

---

## Format attendu pour chaque repas

```
### [Jour] [midi/soir]
**[Nom du plat]**
- Produit exact du catalogue → prix €
- ...

*Préparation :* [étapes simples]

> Perte de poids : [adaptation]

**Coût repas : ~X,XX €**
```

Terminer par un tableau récapitulatif :

| Produit | Qté | Prix unitaire | Total |
|---------|-----|--------------|-------|
| ...     | ... | ...          | ...   |

**TOTAL ~X,XX €**

Si le total dépasse 100 € : proposer une optimisation concrète (substitution de produit moins cher).

---

## Catalogue des produits disponibles

### Boucherie (26 produits)
- Saucisses de Toulouse L'Atelier Boucherie x6 - 750g → 7,99 €
- Chipolatas L'Atelier Boucherie X8 - 520g → 6,83 €
- Saucisses de Toulouse Férial Label Rouge - X4 - 400g → 4,09 €
- Saucisses de Toulouse Férial x4 - 500g → 3,98 €
- Saucisses de Toulouse x4 Soutenons Nos Agriculteurs 400g → 3,97 €
- Chipolatas Férial x6 - 330g → 3,09 €
- Chipolatas Férial x12 - 660g → 5,99 €
- Chipolatas x6 Soutenons Nos Agriculteurs 330g → 4,50 €
- Merguez Férial x12 - 660g → 7,95 €
- Merguez Férial x6 - 330g → 4,79 €
- Plateau Mix Férial 6 chipolatas 6 merguez - 660g → 8,26 €
- Plateau Mix Férial 8 chipolatas 4 merguez - 660g → 7,99 €
- Mini chorizo Férial x8 - 320g → 4,29 €
- Steak de boeuf ** L'Atelier Boucherie x1 - 140g → 3,49 €
- Faux filet de boeuf *** L'Atelier Boucherie x2 - 330g → 8,99 €
- Steak de boeuf** L'Atelier Boucherie x2 - 260g → 6,27 €
- Rumsteck en tournedos*** L'Atelier Boucherie x2 - 280g → 7,29 €
- Faux-filet de boeuf*** L'Atelier Boucherie x1 - 180g → 5,39 €
- Bavette d'Aloyau*** L'Atelier Boucherie x1 - 150g → 4,95 €
- Entrecôte de boeuf*** L'Atelier Boucherie x1 - 200g → 6,19 €
- Rôti de boeuf*** L'Atelier Boucherie - 600g → 14,39 €
- Bavette d'Aloyau *** limousine L'atelier Boucherie - 120G → 5,99 €
- Steak de bœuf ** limousine L'atelier Boucherie x2 - 260G → 7,49 €
- Faux filet bœuf *** limousine L'atelier Boucherie x1 -180G → 6,49 €
- Sauces gourmandes Rustica Pour viande 4 saveurs - 4x90g → 2,34 €
- Frites Pom'lisse 2.5 kg → 3,99 €

### Conserves (31 produits)
> ⚠️ **TOUTES les ratatouilles contiennent des tomates → INTERDITES**
- ~~Ratatouille Notre Jardin A la provençale - 750g~~ → EXCLUE (tomates)
- ~~Ratatouille Notre Jardin A la provençale - 375g~~ → EXCLUE (tomates)
- ~~Ratatouille Bio Village Bio A la provençale - 650g~~ → EXCLUE (tomates)
- ~~Ratatouille Eco+ 750g~~ → EXCLUE (tomates)
- ~~Ratatouille à la Provençale NRT 650g~~ → EXCLUE (tomates)
- ~~Ratatouille Cuisinée Cassegrain à la Provençale 660g~~ → EXCLUE (tomates)
- ~~Ratatouille Cuisinée Cassegrain à la Provençale 380g~~ → EXCLUE (tomates)
- ~~Ratatouille Cuisinée Cassegrain à la Provençale 185g~~ → EXCLUE (tomates)
- ~~Ratatouille niçoise D'aucy 750g~~ → EXCLUE (tomates)
- ~~Ratatouille provençale d'aucy 42,5cl~~ → EXCLUE (tomates)
- ~~Ratatouille Jardin Bio' A la provençale bio - 650g~~ → EXCLUE (tomates)
- Legumes couscous Cassegrain 430g → 2,72 € ⚠️ vérifier composition (risque tomates)
- Légumes couscous Notre Jardin 400g → 1,38 € ⚠️ vérifier composition
- Légumes pour Couscous D'Aucy Orientale - 800g → 1,82 € ⚠️ vérifier composition
- Légumes pour couscous bio Jardin Bio - 660g → 2,68 € ⚠️ vérifier composition
- Le Haricot vert Cueilli Main Bonduelle Extra Fin 280g → 2,52 €
- Courgettes Cuisinées Cassegrain à la Provençale 375g → 3,20 € ⚠️ vérifier composition
- Courgettes Cuisinées Cassegrain à la Provençale 185g → 2,22 € ⚠️ vérifier composition
- ~~Courgettes cuisinées D'Aucy Provencale - 380g~~ → EXCLUE par précaution (risque tomates)
- Aubergines Cuisinées Cassegrain à la Provençale 375g → 3,08 € ⚠️ vérifier composition
- Aubergines compotées & blé Cassegrain - 375g → 3,54 €
- Aubergines Cuisinées Cassegrain à la Provençale 185g → 2,38 € ⚠️ vérifier composition
- Aubergines cuisinées D'Aucy 380g → 2,05 €
- Champignon Bonduelle Emincé - 3x115g → 2,77 €
- Macédoine légumes Notre Jardin - 530g → 1,23 €
- Macédoine légumes Notre Jardin 265g → 0,71 €
- Macédoine légumes Notre Jardin 3x130g → 1,72 €
- Macedoine de legumes Eco 530g → 1,09 €
- Macédoine déjà égouttée D'aucy 265g → 1,35 €
- Macédoine déjà égouttée D'aucy 530g → 2,06 €
- Riz long Comptoir du Grain Cuisson rapide - 2kg → 3,32 €

### Légumes frais (66 produits — tomates exclues)
> ⚠️ **Toutes les tomates sont INTERDITES (allergie)**
- Haricots verts éboutés 500g → 5,99 €
- Pousses haricot Mungo Les Crudettes - 250g → 2,16 €
- Radis ronds Panier du Primeur - 250g → 0,99 €
- Courgettes Bio Bio Village Filet - 750g → 2,49 €
- Courgette 1kg → 2,19 €
- Aubergine Bio Bio Village x2 → 2,99 €
- Aubergine 1p → 1,65 €
- Poivron doux jaune 1p → 1,39 €
- Poivron doux rouge 1p → 1,25 €
- Poivron doux vert 1p → 1,29 €
- Poivrons bicolores Eco+ x2 → 0,99 €
- Poivron Bicolore bio Bio Village x2 → 1,99 €
- Mélange de poivrons doux 500g → 2,49 €
- Mini poivrons mélange HVE Panier du Primeur - 200g → 3,99 €
- ~~Tomate Coeur de pigeon Bio Saveol - 250g~~ → EXCLUE (allergie tomates)
- ~~Tomates cerises colorées Panier du Primeur - 350g~~ → EXCLUE
- ~~Tomates cerises allongées Panier du Primeur - 250g~~ → EXCLUE
- ~~Tomates cerises bio Bio Village - 250g~~ → EXCLUE
- ~~Duo coeur de pigeon Bio Savéol 250g~~ → EXCLUE
- ~~Tomate cocktail grappe Filière Panier du Primeur - 500g~~ → EXCLUE
- ~~Tomates cerises gustatives Panier du Primeur - 300g~~ → EXCLUE
- ~~Tomates rondes Eco+ Filet 1kg~~ → EXCLUE
- ~~Tomates allongées Panier du Primeur - 600g~~ → EXCLUE
- ~~Tomates rondes grappe HVE Panier du Primeur - 750g~~ → EXCLUE
- ~~Tomate ronde grappe Bio Village Bio - 500g~~ → EXCLUE
- ~~Tomates Les Originales Panier du Primeur - 750g~~ → EXCLUE
- ~~Tomate côtelée noire de Crimée 500g~~ → EXCLUE
- Concombre Panier du Primeur HVE - x2 → 2,99 €
- Concombre Bio Bio Village x1 → 1,99 €
- Concombre Noa 1 pièce → 3,69 €
- Fenouil 1p → 1,71 €
- Avocats Eco+ Filet x3 → 1,99 €
- Avocats mûrs à point Panier du Primeur x2 → 3,45 €
- Avocat Bio Bio Village En barquette x2 → 3,59 €
- Betterave rouge Notre Jardin Entière cuite sous vide - 500g → 0,69 €
- Betterave rouge Bio Bio Village - 500g → 1,09 €
- Blancs de poireaux filière Panier du Primeur - 500g → 3,49 €
- Carottes Eco+ Sachet de 2kg → 2,49 €
- Carottes filière Panier du Primeur - 1kg → 1,53 €
- Carotte Bio Bio Village 1kg → 1,99 €
- Carotte 2 Kg → 1,79 €
- Baby carottes Notre Jardin 250g → 1,59 €
- Baby carottes Florette 250g → 2,17 €
- Baby Carottes 450g → 3,60 €
- Baby Carottes Ferme à Jules 200g → 1,75 €
- Baby carottes La Ferme à Jules Les Crudettes - 400g → 3,14 €
- Céleri 1 branche → 2,99 €
- Champignons de Paris blancs Panier du Primeur - 400g → 2,39 €
- Champignons de Paris blancs Bio Bio Village - 200g → 2,29 €
- Champignons de Paris bruns Panier du Primeur - 250g → 1,79 €
- Champignons de Paris bruns bio Bio Village - Barquette 200g → 2,29 €
- Cèpes déshydratés Notre Jardin 40g → 3,16 €
- Chou-fleur blanc 1p → 4,99 €
- Chou-fleur Florette 180g → 2,10 €
- Chou rouge émincé Notre Jardin 250g → 0,99 €
- Ail Eco+ Filet 250g → 1,99 €
- Ail blanc Panier du Primeur x3 → 2,99 €
- IGP Ail blanc de Lomagne Nos Régions ont du Talent 320g → 3,99 €
- Ail blanc bio Bio Village 250g → 3,99 €
- Gousses d'ail blanc 150g → 3,32 €
- Ail violet Panier du Primeur x3 (Espagne) → 2,99 €
- Ail violet Panier du Primeur x3 (France) → 2,99 €
- Oignon Cébette 1 botte → 1,57 €
- Oignons jaunes Eco+ 1.5 Kg → 1,69 €
- Oignons jaunes Filière Panier du Primeur Filet 1kg → 1,99 €
- Chèvre à dorer Les Croisés x4 - 100g → 1,75 €

### Pâtes et féculents (25 produits)
- Pâtes Coquillettes Turini 1kg → 1,35 €
- Pâtes Coquillettes Turini 500g → 0,75 €
- Pâtes Torsades Turini 1kg → 1,17 €
- Pâtes Torsades Turini 500g → 0,59 €
- Pâtes Torsades Turini Nature tomate épinard - 500g → 1,07 € ⚠️ contient tomate → EXCLUE
- Pâtes Penne Regate Turini 500g → 0,59 €
- Mini penne Turini 500g → 0,97 €
- Mini farfalle Turini 500g → 1,09 €
- Pâtes Farfalles Turini 1kg → 1,20 €
- Pâtes Coudes Rayés Turini 1kg → 1,75 €
- Mini coudes Turini 500g → 0,97 €
- Pâtes serpentini Turini 500g → 0,85 €
- Pâtes gansettes Turini 500g → 0,97 €
- Pâtes Macaroni Turini 1kg → 1,35 €
- Pâtes Macaroni Turini 500g → 0,75 €
- Pâtes Tagliatelles Turini 500g → 1,19 €
- Pâtes Nouilles Turini 500g → 0,75 €
- Spaghetti Turini 500g → 0,69 €
- Pâtes Spaghetti Turini 1kg → 1,33 €
- Pâtes linguine Turini 500g → 0,90 €
- Pâtes Capellini Turini 500g → 0,85 €
- Pâtes Alphabet Turini 500g → 0,95 €
- Pâtes Etoiles Turini 500g → 0,99 €
- Muscade Noix Entières Ducros 18 g → 2,66 €

### Poissonnerie (26 produits)
- Queues de langouste crue Ronde des Mers - 340g → 23,79 €
- Crevette cuite 60/80 Equat ASC L'Atelier Poissonnerie - 500g → 4,99 €
- Crevettes natures Pêche Océan 125g → 3,99 €
- Crevettes décortiquées ASC Delpierre - 180g → 6,42 €
- Couronne de crevettes Delpierre ASC Sauce cocktail - 130g → 5,12 €
- Crevettes Delpierre ASC décortiquées - 100g → 3,67 €
- Couronne de crevettes Delpierre ASC sauce fines herbes - 130g → 5,06 €
- Crevettes nature Assiette Bleue Décortiquées - 200g → 6,52 €
- Crevettes décortiquées ASC Delpierre Ail et Persil 180g → 6,11 €
- Sauce Mayonnaise La Sablaise 135g → 2,25 €
- Filet de maquereaux Pêche Océan Fumé poivre - 150g → 3,29 €
- Filets de Morue Ronde des Mers Prêt à cuisiner 400g → 7,99 €
- Mayonnaise Fins Gourmets MAILLE Bocal - 320g → 2,49 €
- Pavé de saumon Eco+ 4x110g → 8,98 €
- Pavé de saumon Eco+ 2x110g → 4,97 €
- Dos de cabillaud MSC Eco+ Sans peau et sans arête - 200g → 5,99 €
- Pavés de saumon Global Gap L'Atelier Poissonnerie x4 -500g → 11,49 €
- Pavé de saumon élevé en Norvège L'Atelier Poissonnerie x6 -750g → 16,40 €
- Pavés de saumon Global Gap L'Atelier Poissonnerie x2 250g → 5,99 €
- Filet de saumon de Norvège Global Gap - 600g → 12,95 €
- Dos de cabillaud MSC L'Atelier Poissonnerie - 300g → 10,99 €
- Filets de colin d'Alaska Meunière MSC x2 - 200g → 2,69 €
- Filets de limande du Nord MSC L'Atelier Poissonnerie x4 400g → 6,75 €
- Filets de limande du Nord MSC L'Atelier Poissonnerie x2 200g → 3,49 €
- Citron à jus Filière Panier du Primeur Sachet 1kg → 3,69 €
- Crevettes décortiquées Eco+ 500g → 4,99 €

### Volaille (25 produits)
- Saucisse de volaille Volandrie x6 - 300g → 3,49 €
- Filet de poulet Bon Plan Douce France - 500g → 5,67 €
- Cuisses de poulet Bon Plan Douce France - 900g → 4,62 €
- Émincés de poulet paprika L'Atelier Volaille - 300g → 3,79 €
- Filet de poulet blanc Volandrie Extra tendre - 300g → 3,90 €
- Filet de poulet jaune Volandrie Extra tendre - 300g → 3,90 €
- Aiguillettes poulet blanc Volandrie - 210g → 2,95 €
- Aiguillettes poulet jaune Volandrie - 210g → 2,95 €
- Filets poulet blanc Volandrie 300g → 3,79 €
- Filet de poulet jaune Volandrie 300g → 3,79 €
- Filet de poulet blanc St Charmin Blanc Val de Loire x2 - 240g → 5,49 €
- Cuisse de poulet St Charmin Blanc Val de Loire x2 - 480g → 4,08 €
- Filets de poulet St Charmin Val de Loire x2 - 240g → 5,49 €
- Filets de poulet Périgord NRT x2 Label Rouge - 265g → 6,15 €
- Filets de poulet Auvergne NRT x2 Label Rouge - 265g → 6,15 €
- Filets de poulet Eco+ Blanc - 1kg → 9,49 €
- Haut de cuisse Maitre Coq Poulet blanc nourri au blé 750g → 4,11 €
- Haut de cuisse jaune Maitre Coq Poulet nourri au maïs - 750g → 4,56 €
- Filet de poulet blanc Maitre Coq nourri blé 300g → 4,15 €
- Filet de poulet jaune Maitre Coq nourri mais 300g → 4,44 €
- Cuisse de poulet blanc Maître Coq - 1kg → 5,86 €
- Cuisse de poulet Maitre Coq Jaune nourri maïs - 1kg → 5,25 €
- Pilon de poulet Maitre Coq Jaune nourri au maïs - 750g → 4,64 €
- Mayonnaise Rustica 830g → 3,65 €
- Pommes frites Eco+ 2,5kg → 2,67 €

### Fruits (23 produits)
- Duo Raisins Sans Pepin - 500g → 2,99 €
- Myrtilles Panier du Primeur 125g → 1,99 €
- Mûre Panier du Primeur 125g → 2,49 €
- Framboises Panier du Primeur 125g → 1,99 €
- Groseilles Panier du Primeur 125g → 2,99 €
- Melon Eco+ x1 → 0,99 €
- Melon HVE Panier du Primeur x1 → 2,49 €
- Melon Charentais bio Bio Village x1 → 3,49 €
- Melon Charentais 1p → 3,10 €
- Melon Galia 1p → 1,99 €
- Melon jaune 1p → 2,49 €
- Melon vert 1p → 2,49 €
- Kiwi sungold Zespri 1p → 0,80 €
- Mini pastèque Panier du Primeur x1 → 3,17 €
- Mini pastèque Bio Village Bio x1 → 3,49 €
- Pastèque jaune La pièce → 5,32 €
- Abricots Eco+ Barquette 1kg → 2,99 €
- Abricots des Baronnies Nos Régions ont du Talent 500g → 4,99 €
- Nectarines Eco+ Barquette 1kg → 2,99 €
- Nectarines blanches Filière Panier du Primeur Barquette x4 → 3,89 €
- Nectarines jaune Filière Panier du Primeur Barquette x4 → 3,89 €
- Nectarines Bio Village x4 → 4,49 €
- Nectarine jaune 1p → 0,64 €

---

## Instructions finales

1. Utilise **uniquement** les produits listés ci-dessus.
2. Indique le **nom exact** du produit tel qu'il apparaît dans le catalogue.
3. Respecte **toutes** les contraintes sans exception.
4. Calcule le coût de chaque repas et le total de la liste de courses.
5. Signale en rouge tout produit dont la composition mérite vérification (risque tomates caché).
6. Propose **au moins 2 repas simples** (< 10 min).
