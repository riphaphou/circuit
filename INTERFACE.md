# Circuit Designer - Interface Utilisateur

## Vue d'Ensemble de l'Interface

L'application Circuit Designer présente une interface graphique complète organisée en 5 zones principales:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ [📄 Nouveau] [📁 Ouvrir] [💾 Sauvegarder] [🧹 Effacer] [🔬 Calculer]    │
│                                              Circuit Designer v1.0     │
├──────────┬────────────────────────────────────────────┬─────────────────┤
│          │                                            │                 │
│ PALETTE  │            CANVAS PRINCIPAL                │   PROPRIÉTÉS    │
│          │                                            │                 │
│ ┌──────┐ │                                            │ Composant: R1   │
│ │Résis.│ │     ┌────────┐     ┌────────┐            │ Type: Resistor  │
│ └──────┘ │     │   12V  │─────│  1kΩ   │            │ Valeur: 1000    │
│ ┌──────┐ │     │ V1 ⊕⊖  │     │   R1   │            │ Unité: Ω        │
│ │Voltag│ │     └────────┘     └────────┘            │ Position X: 300 │
│ └──────┘ │                                            │ Position Y: 200 │
│ ┌──────┐ │                                            │                 │
│ │Couran│ │                                            │ [Appliquer]     │
│ └──────┘ │     [Grille 20x20 pixels]                 │ [Supprimer]     │
│ ┌──────┐ │                                            │                 │
│ │Condo.│ │                                            │                 │
│ └──────┘ │                                            │                 │
│ ┌──────┐ │                                            │                 │
│ │Induct│ │                                            │                 │
│ └──────┘ │                                            │                 │
│ ┌──────┐ │                                            │                 │
│ │ Fil  │ │                                            │                 │
│ └──────┘ │                                            │                 │
│          │                                            │                 │
├──────────┴────────────────────────────────────────────┴─────────────────┤
│                        RÉSULTATS DES CALCULS                            │
│                                                                          │
│ === Résultats des calculs ===                                          │
│                                                                          │
│ Tension totale: 12.000 V                                               │
│ Courant total: 0.012000 A                                              │
│ Puissance totale: 0.144000 W                                           │
│ Résistance équivalente: 1000.000 Ω                                     │
│                                                                          │
│ --- Composants ---                                                      │
│ R1: Tension: 12.000 V, Courant: 0.012000 A, Puissance: 0.144000 W    │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

## Description des Zones

### 1. Barre d'Outils (Haut)
- **Boutons d'action rapide**:
  - 📄 Nouveau circuit
  - 📁 Ouvrir un fichier
  - 💾 Sauvegarder
  - 🧹 Effacer tout
  - 🔬 Calculer
- **Informations**: Version de l'application

### 2. Palette de Composants (Gauche)
- **Titre**: "Composants"
- **Boutons colorés** pour chaque type:
  - Résistance (beige)
  - Source de Tension (rose)
  - Source de Courant (bleu clair)
  - Condensateur (violet)
  - Inductance (vert)
  - Fil (gris)
- **Instructions**: Guide d'utilisation rapide

### 3. Canvas Principal (Centre)
- **Zone de dessin** blanche avec grille
- **Grille magnétique** (snap-to-grid) 20x20 pixels
- **Composants dessinés** avec symboles standards:
  - Sources: Cercles avec polarité (+/-)
  - Résistances: Rectangles
  - Condensateurs: Deux lignes parallèles
  - Inductances: Spirales (arcs)
- **Interaction**:
  - Clic pour placer
  - Glisser-déposer pour déplacer
  - Clic droit pour sélectionner

### 4. Panneau de Propriétés (Droite)
- **Titre**: "Propriétés"
- **Champs d'information**:
  - Nom du composant (éditable)
  - Type (lecture seule)
  - Valeur (éditable)
  - Unité (lecture seule)
  - Position X, Y (lecture seule)
- **Boutons d'action**:
  - Appliquer: Valider les modifications
  - Supprimer: Effacer le composant

### 5. Zone de Résultats (Bas)
- **Titre**: "Résultats des calculs"
- **Affichage formaté** des résultats:
  - Grandeurs globales (V, I, P, Req)
  - Détails par composant
  - Formatage avec précision adaptée
- **Scrollbar** pour résultats longs

## Symboles des Composants

### Résistance
```
    ┌──────────────┐
────┤              ├────
    │      R1      │
    │    1000Ω     │
    └──────────────┘
```

### Source de Tension
```
        ╭─────╮
    ────┤  +  │────
        │ 12V │
        │  -  │
        ╰─────╯
```

### Source de Courant
```
        ╭─────╮
    ────┤  →  │────
        │ 1mA │
        ╰─────╯
```

### Condensateur
```
        │  │
    ────┤  ├────
        │  │
       1µF
```

### Inductance
```
        ╭──╮╭──╮
    ────╯  ╰╯  ╰────
         1mH
```

## Couleurs et Style

### Palette de Composants
- **Résistance**: #FFE4B5 (Beige)
- **Source de Tension**: #FFB6C1 (Rose)
- **Source de Courant**: #B0E0E6 (Bleu clair)
- **Condensateur**: #DDA0DD (Violet)
- **Inductance**: #98FB98 (Vert)
- **Fil**: #D3D3D3 (Gris)

### Canvas
- **Fond**: Blanc (#FFFFFF)
- **Grille**: Gris clair (#E0E0E0)
- **Composants**: Noir (#000000)
- **Terminaux**: Rouge (#FF0000)

### Résultats
- **Fond**: Gris très clair (#F0F0F0)
- **Texte**: Noir, police monospace

## Menus

### Menu Fichier
```
Fichier
├── Nouveau          (Ctrl+N)
├── Ouvrir...        (Ctrl+O)
├── Sauvegarder      (Ctrl+S)
├── Sauvegarder sous...
├── ──────────────
└── Quitter          (Ctrl+Q)
```

### Menu Édition
```
Édition
└── Effacer tout
```

### Menu Circuit
```
Circuit
├── Calculer         (F5)
└── Analyser
```

### Menu Aide
```
Aide
├── À propos
└── Guide d'utilisation
```

## Interactions Utilisateur

### Ajouter un Composant
1. Clic sur le composant dans la palette → curseur en croix
2. Clic sur le canvas → composant placé
3. Composant ajouté avec valeurs par défaut

### Modifier un Composant
1. Clic droit sur le composant → sélection
2. Propriétés affichées à droite
3. Modification des valeurs
4. Clic "Appliquer" → mise à jour

### Déplacer un Composant
1. Clic gauche maintenu sur le composant
2. Déplacement de la souris
3. Relâchement → nouvelle position (snap-to-grid)

### Supprimer un Composant
1. Sélection (clic droit)
2. Clic "Supprimer" dans le panneau
3. Confirmation → suppression

### Calculer le Circuit
1. Circuit créé avec source + résistances
2. Clic "Calculer" ou F5
3. Résultats affichés en bas
4. Vérification de validité automatique

## Formats de Fichier

### Structure JSON
```json
{
  "components": [
    {
      "type": "VoltageSource",
      "id": 1,
      "name": "V1",
      "value": 12,
      "x": 100,
      "y": 200,
      "connections": [],
      "polarity": "+"
    },
    {
      "type": "Resistor",
      "id": 2,
      "name": "R1",
      "value": 1000,
      "x": 300,
      "y": 200,
      "connections": []
    }
  ],
  "wires": []
}
```

## Messages et Dialogues

### Messages d'Information
- "Circuit sauvegardé avec succès"
- "Calculs terminés"
- "Propriétés mises à jour"

### Messages d'Avertissement
- "Circuit invalide: Aucune source de tension ou courant"
- "Aucun composant sélectionné"
- "Résistance a une valeur invalide"

### Messages d'Erreur
- "Impossible de charger le circuit"
- "Impossible de sauvegarder le circuit"
- "Valeur invalide"

### Confirmations
- "Créer un nouveau circuit?"
- "Effacer tout le circuit?"
- "Supprimer R1?"
- "Voulez-vous vraiment quitter?"

## Accessibilité

### Raccourcis Clavier
- Toutes les fonctions principales accessibles par raccourcis
- Accélérateurs dans les menus (soulignés)
- Navigation au clavier possible

### Retour Visuel
- Curseur change selon le mode (normal/placement)
- Composant sélectionné visible dans les propriétés
- Messages de confirmation pour les actions

### Responsive
- Fenêtre redimensionnable
- Canvas s'adapte à la taille
- Panneaux latéraux à largeur fixe
- Scrollbars si nécessaire

---

Cette interface a été conçue pour être:
- ✅ **Intuitive**: Tout est à portée de clic
- ✅ **Efficace**: Raccourcis pour les actions fréquentes
- ✅ **Claire**: Zones bien délimitées
- ✅ **Professionnelle**: Symboles standards électroniques
- ✅ **Accessible**: Multiples moyens d'accès aux fonctions
