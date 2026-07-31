# Leclerc Drive — Menu Semaine

Projet de génération automatique de menus familiaux à partir du catalogue Leclerc Drive de Mougins.

---

## TL;DR

1. Sauvegarder les pages HTML depuis leclercdrive.fr dans ce dossier
2. Dire à OpenCode : **"J'ai mis à jour mes HTML, régénère le menu et le prompt"**
3. C'est tout — `products.json`, `menu_semaine.md` et `chatgpt_prompt.md` sont régénérés

---

## Comment ça marche

1. Sauvegarder les pages HTML depuis leclercdrive.fr
2. Lancer le script d'extraction
3. Demander à OpenCode de régénérer le menu et le prompt

---

## Structure du projet

```
.
├── *.html                  # Pages HTML sauvegardées depuis leclercdrive.fr
├── extract_legumes.py      # Script d'extraction des produits
├── products.json           # Catalogue produits généré (ne pas éditer)
├── menu_constraints.md     # Contraintes du menu (à éditer si besoin)
├── menu_semaine.md         # Menu de la semaine généré
├── chatgpt_prompt.md       # Prompt ChatGPT généré
├── opencode.json           # Config OpenCode
└── .opencode/
    └── skills/
        └── leclerc-menu/
            └── SKILL.md    # Skill OpenCode
```

---

## Pages HTML à sauvegarder

Aller sur chaque page, faire `Cmd+S` (HTML uniquement), sauvegarder dans ce dossier :

| Fichier | URL |
|---|---|
| `legumes.html` | `.../rayon-284351-Legumes.aspx` |
| `fruits.html` | `.../rayon-fruits.aspx` |
| `boucherie.html` | `.../rayon-boucherie.aspx` |
| `conserves.html` | `.../rayon-conserves.aspx` |
| `pates.html` | `.../rayon-pates.aspx` |

> Ajouter autant de pages que souhaité — le script traite automatiquement tous les fichiers `*.html` du dossier.

---

## Régénérer les produits

```bash
python3 extract_legumes.py
```

Génère `products.json` avec tous les produits disponibles (prix, catégorie, origine).

> Les produits en rupture de stock (`data-vignette="vide"`) sont ignorés automatiquement — ils apparaissent dans le HTML mais sans prix.

---

## Régénérer le menu et le prompt

Dire à OpenCode :

> "J'ai mis à jour mes HTML, régénère le menu et le prompt"

OpenCode va :
1. Relancer `extract_legumes.py`
2. Lire `menu_constraints.md`
3. Régénérer `menu_semaine.md`
4. Régénérer `chatgpt_prompt.md`

---

## Contraintes du menu (`menu_constraints.md`)

- 4 personnes : 2 adultes + 2 enfants (5 et 8 ans)
- 1 adulte en perte de poids
- 1 enfant à surveiller
- **Allergie tomates** — aucune tomate sous aucune forme
- Semaine : dîner uniquement (lun → ven)
- Week-end : déjeuner + dîner (sam + dim)
- Budget max : 100 €/semaine
- Préparation max : 20 minutes
- Équilibre : 1/4 viande · 1/4 féculent · 1/2 légume
- Inclure des repas simples (ex. steak + haricots verts + riz, < 10 min)

---

## ⚠️ Allergie tomates

**Les tomates sont une allergie — pas une préférence.**

Produits à risque à vérifier systématiquement :
- Toutes les **ratatouilles** en conserve → contiennent des tomates → **INTERDITES**
- Courgettes cuisinées D'Aucy → vérifier l'étiquette
- Légumes pour couscous → vérifier l'étiquette

---

## Modifier les contraintes

Éditer `menu_constraints.md` puis demander à OpenCode de régénérer le menu.
