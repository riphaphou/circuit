# Exemples d'images de fond

Ce répertoire contient des images d'exemple pour personnaliser l'arrière-plan du canvas.

## Images disponibles

### 1. grid_pattern.png
Grille technique classique avec lignes fines et épaisses.
- Fond blanc
- Grille gris clair (tous les 20px)
- Grille gris foncé (tous les 100px)
- Idéal pour : Travail de précision

### 2. blueprint.png
Style plan technique / blueprint.
- Fond bleu foncé (#0D3B66)
- Grille bleu clair
- Points de référence aux intersections
- Idéal pour : Style professionnel

### 3. circuit_board.png
Motif de circuit imprimé (PCB).
- Fond vert (#1A5F3A)
- Traces dorées simulées
- Points de soudure argentés
- Idéal pour : Ambiance électronique

### 4. gradient.png
Dégradé doux du bleu clair au blanc.
- Transition douce
- Aucune distraction
- Idéal pour : Confort visuel

## Utilisation

1. Lancez l'application : `python main.py`
2. Menu **Apparence** → **Charger image de fond...**
3. Sélectionnez une image dans ce dossier
4. Ajustez l'opacité et le mode via **Personnaliser...**

## Modes d'affichage

- **Stretch** : Étire l'image pour remplir le canvas
- **Tile** : Répète l'image en mosaïque
- **Center** : Centre l'image sans déformation

## Créer vos propres images

Vous pouvez créer vos propres images de fond :

- Formats supportés : PNG, JPG, JPEG, GIF, BMP
- Taille recommandée : 400x400 pixels ou plus
- Couleurs : Privilégier des couleurs douces pour ne pas gêner la lecture du circuit

### Exemple avec Python :

```python
from PIL import Image, ImageDraw

# Créer une image
img = Image.new('RGB', (400, 400), color='#E8F5E9')
draw = ImageDraw.Draw(img)

# Dessiner un motif
for i in range(0, 400, 20):
    draw.line([(i, 0), (i, 400)], fill='#C8E6C9', width=1)
    draw.line([(0, i), (400, i)], fill='#C8E6C9', width=1)

# Sauvegarder
img.save('mon_motif.png')
```

## Régénérer les images

Pour régénérer toutes les images d'exemple :

```bash
python generate_backgrounds.py
```
