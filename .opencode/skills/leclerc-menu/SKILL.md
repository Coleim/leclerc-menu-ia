---
name: leclerc-menu
description: Use when working on the Leclerc Drive project in /Users/coliva/dev/perso/leclerc. Handles regenerating products.json from HTML files, regenerating the weekly menu (menu_semaine.md), and regenerating the ChatGPT prompt (chatgpt_prompt.md). Trigger keywords: leclerc, menu, courses, html, produits, régénérer, semaine.
---

# Leclerc Menu Skill

Ce skill gère le projet Leclerc Drive : extraction des produits depuis les HTML sauvegardés, génération du menu de la semaine et du prompt ChatGPT.

## Structure du projet

```
/Users/coliva/dev/perso/leclerc/
├── *.html                  # Pages sauvegardées depuis leclercdrive.fr
├── extract_legumes.py      # Script d'extraction → products.json
├── products.json           # Catalogue produits généré
├── menu_constraints.md     # Contraintes du menu (source de vérité)
├── menu_semaine.md         # Menu généré
└── chatgpt_prompt.md       # Prompt ChatGPT généré
```

## Workflow complet

Quand l'utilisateur dit "régénère", "j'ai mis à jour les HTML", ou demande un nouveau menu, exécuter dans cet ordre :

### Étape 1 — Régénérer products.json

```bash
cd /Users/coliva/dev/perso/leclerc && python3 extract_legumes.py
```

Vérifier que le nombre de produits par catégorie est cohérent. Si une catégorie a très peu de produits (< 5), signaler que certains sont peut-être en rupture de stock (`data-vignette="vide"`).

### Étape 2 — Régénérer menu_semaine.md

Lire `menu_constraints.md` et `products.json`, puis générer `menu_semaine.md` en respectant **toutes** les règles ci-dessous.

### Étape 3 — Régénérer chatgpt_prompt.md

Générer `chatgpt_prompt.md` avec le catalogue complet des produits disponibles et toutes les contraintes.

---

## Règles de génération du menu

### Contraintes dures (JAMAIS violer)

- **ALLERGIE TOMATES** : zéro tomate, sous aucune forme. Ni fraîche, ni en conserve, ni en sauce, ni en ingrédient caché. Les ratatouilles contiennent des tomates → **INTERDITES**. Vérifier aussi : courgettes cuisinées D'Aucy (peuvent contenir des tomates), légumes couscous (vérifier). En cas de doute sur une conserve, l'exclure ou ajouter un avertissement explicite en rouge.
- **4 personnes** : 2 adultes + 2 enfants (5 et 8 ans)
- **Budget** : max 100 € total pour la semaine
- **Temps** : max 20 min de préparation active

### Contraintes de santé

- 1 adulte en perte de poids → préciser à chaque repas : réduire/supprimer le féculent, doubler les légumes
- 1 enfant à surveiller → pas d'épices fortes, pas de sauce grasse, portions adaptées
- Équilibre assiette : 1/4 protéine · 1/4 féculent · 1/2 légume

### Structure de la semaine

- **Lundi → Vendredi** : dîner uniquement (5 repas)
- **Samedi + Dimanche** : déjeuner ET dîner (4 repas)
- Total : 9 repas

### Variété et simplicité

- Ne pas répéter la même protéine deux jours consécutifs
- **Inclure au moins 1-2 repas très simples dans la semaine** : ex. haricots verts + riz + steak, pâtes + beurre + légumes vapeur. Préparation < 10 min, ingrédients basiques.
- Varier les légumes : utiliser carottes, poireaux, courgettes, champignons, poivrons, haricots verts, etc.
- Éviter de toujours utiliser les mêmes produits

### Format de chaque repas

```
### [Jour] [midi/soir]
**[Nom du plat]**
- Produit exact du catalogue → prix €
- ...

*Préparation :* [étapes simples]

> Perte de poids : [adaptation]

**Coût repas : ~X,XX €**
```

### Liste de courses

Tableau avec : Produit | Qté | Prix unitaire | Total
Ligne finale : **TOTAL ~X,XX €**

Si total > 100 € : proposer une optimisation concrète (substitution de produit).

---

## Règles de génération du prompt ChatGPT

Le prompt doit :
1. Expliquer le rôle (nutritionniste + chef familial)
2. Lister toutes les contraintes en détail
3. Mentionner l'**ALLERGIE TOMATES** en majuscules et en gras, avec exemples de produits à risque
4. Inclure le catalogue complet des produits disponibles avec prix (généré depuis `products.json`)
5. Demander le format exact : repas par repas + liste de courses + total
6. Demander des suggestions de repas simples (< 10 min)

---

## Notes importantes

- Les produits avec `data-vignette="vide"` dans le HTML sont en rupture de stock et ne sont pas extraits par le script → normal.
- Le script `extract_legumes.py` traite **tous** les fichiers `*.html` du répertoire automatiquement.
- `menu_constraints.md` est la source de vérité pour les contraintes — toujours le relire avant de générer.
