# Guide d'Utilisation - Circuit Designer (Après Corrections)

## Interface Principale

```
╔══════════════════════════════════════════════════════════════════════════════╗
║ Circuit Designer - Outil de conception de circuits électroniques            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ 📄 Nouveau │ 📁 Ouvrir │ 💾 Sauvegarder │ | 🧹 Effacer │ 🔬 Calculer  v1.0 ║
╠══════════╦═══════════════════════════════════════════════════════╦══════════╣
║ Palette  ║                    Circuit                            ║Propriétés║
║          ║                                                        ║          ║
║ [Résis-  ║  ┌────────────────────────────────────────────┐      ║ Nom: R1  ║
║  tance]  ║  │                                             │      ║          ║
║          ║  │   • • • • • • • • • • • • • • • • • • •    │      ║ Valeur:  ║
║ [Source  ║  │   • • • • • • • • • • • • • • • • • • •    │      ║ 100 Ω    ║
║  Tension]║  │   • • • •  ┌─────┐ • • • • • • • • • •    │      ║          ║
║          ║  │   • • • • •│ R1  │ • • • • • • • • • •    │      ║ Position:║
║ [Source  ║  │   • • • •  └─────┘ • • • • • • • • • •    │      ║ (140,100)║
║  Courant]║  │   • • • • • • • • • • • • • • • • • • •    │      ║          ║
║          ║  │   • • • • • • ⊕ • • • • • • • • • • • •    │      ║          ║
║ [Conden- ║  │   • • • • •  V1  • • • • • • • • • • •    │      ║          ║
║  sateur] ║  │   • • • • • • ⊖ • • • • • • • • • • • •    │      ║          ║
║          ║  │   • • • • • • • • • • • • • • • • • • •    │      ║          ║
║ [Induc-  ║  │   • • • • • • • • • • • • • • • • • • •    │      ║          ║
║  tance]  ║  │   • • • • • • • • • • • • • • • • • • •    │      ║          ║
║          ║  │   • • • • • • • • • • • • • • • • • • •    │      ║          ║
║ [Fil]    ║  │                                             │      ║          ║
║          ║  └────────────────────────────────────────────┘      ║          ║
║          ║      ← Canvas s'étend avec la fenêtre →              ║          ║
╠══════════╩═══════════════════════════════════════════════════════╩══════════╣
║ Résultats des calculs                                                        ║
║ ┌──────────────────────────────────────────────────────────────────────────┐ ║
║ │ Courant total: 0.5 A                                                     │ ║
║ │ Tension aux bornes de R1: 50 V                                           │ ║
║ │ Puissance dissipée: 25 W                                                 │ ║
║ └──────────────────────────────────────────────────────────────────────────┘ ║
╚══════════════════════════════════════════════════════════════════════════════╝

Largeur fixe     Extensible (prend tout l'espace)     Largeur fixe
   ~150px                                                  ~200px
```

## Fonctionnalités Corrigées

### ✅ 1. Canvas Responsive

**Avant:**
- Canvas fixe à 700x500 pixels
- Grande zone noire inutilisée
- Pas de redimensionnement

**Après:**
- Canvas prend TOUT l'espace disponible
- S'adapte au redimensionnement de la fenêtre
- Grille redimensionnée automatiquement
- Utilise grid layout avec `weight=10` pour la colonne centrale

**Code:**
```python
# Configuration du grid
main_frame.grid_columnconfigure(1, weight=10)  # Canvas extensible
canvas.grid(row=0, column=0, sticky='nsew')    # S'étend dans toutes les directions
```

### ✅ 2. Placement de Composants

**Avant:**
- Cliquer sur les boutons ne faisait rien
- Conflits de bindings d'événements

**Après:**
1. Cliquer sur "Résistance" → curseur devient une croix (crosshair)
2. Cliquer sur le canvas → composant placé à cette position
3. Curseur redevient normal
4. Alignement automatique sur la grille (snap-to-grid)

**Flux:**
```
Bouton "Résistance" 
    ↓
canvas.set_component_to_place(Resistor)
    ↓
Curseur = crosshair
    ↓
Clic sur canvas
    ↓
canvas.add_component(Resistor, x, y)
    ↓
Composant dessiné + ajouté au circuit manager
    ↓
Mode placement désactivé, curseur normal
```

### ✅ 3. Création de Fils

**Mode opératoire:**
1. Cliquer sur le bouton "Fil"
2. Le curseur change en "plus" (+)
3. Cliquer sur un premier composant → fil démarre
4. Ligne jaune pointillée suit la souris
5. Cliquer sur un deuxième composant → fil créé
6. Mode fil désactivé automatiquement

**Code:**
```python
# Activation du mode
canvas.start_wire_mode()

# Premier clic
wire_start = (composant1, x1, y1)
temp_wire_id = canvas.create_line(..., dash=(5, 5))

# Déplacement de la souris
canvas.coords(temp_wire_id, x1, y1, x_souris, y_souris)

# Deuxième clic
wire = Wire(start_comp=comp1, end_comp=comp2)
wire.set_endpoints(comp1.x, comp1.y, comp2.x, comp2.y)
circuit_manager.add_component(wire)
```

### ✅ 4. Déplacement de Composants

**Mode opératoire:**
1. Cliquer et maintenir sur un composant
2. Déplacer la souris
3. Le composant suit
4. Relâcher pour positionner

**Note:** Le déplacement fonctionne quand on n'est pas en mode placement ou en mode fil.

## Structure du Layout

### Grid Configuration

```python
# Fenêtre principale
root.grid_rowconfigure(0, weight=0)  # Toolbar (hauteur fixe)
root.grid_rowconfigure(1, weight=1)  # Contenu (extensible)
root.grid_rowconfigure(2, weight=0)  # Résultats (hauteur fixe)

# Frame principal
main_frame.grid_columnconfigure(0, weight=0)   # Palette ~150px
main_frame.grid_columnconfigure(1, weight=10)  # Canvas (extensible)
main_frame.grid_columnconfigure(2, weight=0)   # Propriétés ~200px
```

### Hiérarchie des Widgets

```
MainWindow (Tk)
├── Toolbar (Frame, row=0)
│   └── Boutons (pack inside)
├── MainFrame (Frame, row=1, weight=1)
│   ├── Palette (LabelFrame, col=0, width=150, fixed)
│   │   └── ComponentPalette
│   │       └── Boutons pour chaque composant
│   ├── CenterPanel (LabelFrame, col=1, sticky='nsew')
│   │   └── CircuitCanvas (Canvas, sticky='nsew')
│   │       ├── Grille (redimensionnable)
│   │       ├── Composants
│   │       └── Fils
│   └── PropertiesPanel (LabelFrame, col=2, width=200, fixed)
│       └── Infos sur composant sélectionné
└── ResultsFrame (LabelFrame, row=2)
    └── Text widget avec résultats des calculs
```

## Modes d'Interaction

### Mode Normal (par défaut)
- Curseur: flèche normale
- Clic sur composant: commence le drag
- Drag: déplace le composant
- Release: positionne le composant

### Mode Placement de Composant
- Curseur: crosshair (croix)
- Activé par: clic sur bouton composant (sauf "Fil")
- Clic sur canvas: place le composant
- Retour automatique au mode normal

### Mode Création de Fil
- Curseur: plus (+)
- Activé par: clic sur bouton "Fil"
- Premier clic sur composant: démarre le fil
- Mouvement souris: ligne pointillée suit
- Deuxième clic sur composant: crée le fil
- Retour automatique au mode normal

## Tests de Validation

### Test 1: Redimensionnement
```
1. Lancer l'application
2. Observer la taille initiale (1200x800)
3. Redimensionner la fenêtre (agrandir)
   ✓ Le canvas s'agrandit
   ✓ La palette reste à ~150px
   ✓ Les propriétés restent à ~200px
   ✓ La grille se redessine
4. Réduire la fenêtre
   ✓ Le canvas se réduit (minimum ~400px)
   ✓ Les panneaux fixes gardent leur taille
```

### Test 2: Placement de Composants
```
Pour chaque type (Résistance, Source Tension, etc.):
1. Cliquer sur le bouton
   ✓ Curseur devient une croix
2. Cliquer sur le canvas
   ✓ Composant apparaît
   ✓ Position alignée sur la grille
   ✓ Curseur redevient normal
3. Le composant est visible et nommé (R1, V1, etc.)
```

### Test 3: Création de Fils
```
1. Placer deux résistances (R1 et R2)
2. Cliquer sur "Fil"
   ✓ Curseur devient +
3. Cliquer sur R1
   ✓ Fil démarre
4. Bouger la souris
   ✓ Ligne jaune pointillée suit
5. Cliquer sur R2
   ✓ Fil créé entre R1 et R2
   ✓ Ligne devient solide noire
   ✓ Mode fil désactivé
```

### Test 4: Déplacement
```
1. Placer une résistance
2. Cliquer et maintenir sur la résistance
3. Déplacer la souris
   ✓ La résistance suit
4. Relâcher
   ✓ La résistance reste à la nouvelle position
```

## Raccourcis Clavier

- `Ctrl+N`: Nouveau circuit
- `Ctrl+O`: Ouvrir un circuit
- `Ctrl+S`: Sauvegarder
- `Ctrl+Q`: Quitter
- `F5`: Calculer le circuit

## Symboles des Composants

### Résistance
```
    R1
  ┌────┐
●─┤    ├─●
  └────┘
   100Ω
```

### Source de Tension
```
    V1
   ╭─╮
 ●─┤+⊖├─●
   ╰─╯
   12V
```

### Source de Courant
```
    I1
   ╭─╮
 ●─┤→ ├─●
   ╰─╯
  50mA
```

### Condensateur
```
    C1
    ││
 ●──┤├──●
    ││
  10µF
```

### Inductance
```
    L1
 ●─⌇⌇⌇⌇─●
  100mH
```

### Fil
```
 ●──────●
  (ligne noire)
```

## Limitations Connues

1. **Déplacement de composants avec fils**: Les fils ne suivent pas encore automatiquement les composants quand on les déplace
2. **Suppression**: Pas encore de fonction pour supprimer un composant ou un fil (prévu: clic droit)
3. **Édition des propriétés**: Le panneau de propriétés affiche mais ne permet pas encore de modifier les valeurs
4. **Annuler/Refaire**: Pas encore implémenté

## Prochaines Améliorations Suggérées

1. **Mise à jour dynamique des fils**: Quand un composant est déplacé, ses fils devraient suivre
2. **Menu contextuel**: Clic droit pour supprimer, éditer, dupliquer
3. **Zoom**: Molette de la souris pour zoomer/dézoomer
4. **Pan**: Clic central pour déplacer la vue
5. **Sélection multiple**: Ctrl+Clic pour sélectionner plusieurs composants
6. **Export d'image**: Sauvegarder le circuit en PNG/SVG

## Architecture Technique

### Gestion des Événements

```python
# Canvas bindings
<Button-1>        → on_click()
<B1-Motion>       → on_drag()
<ButtonRelease-1> → on_release()
<Button-3>        → on_right_click()
<Configure>       → on_resize()
```

### Variables d'État du Canvas

```python
component_to_place: None ou Classe  # Composant à placer au prochain clic
drawing_wire: bool                   # Mode création de fil actif
wire_start: tuple ou None            # (composant, x, y) du départ du fil
temp_wire_id: int ou None            # ID de la ligne temporaire
selected_component: Component        # Composant actuellement sélectionné
drag_data: dict                      # Données pour le drag & drop
```

### Flux de Données

```
User Action
    ↓
GUI Event (click, drag, etc.)
    ↓
Canvas Event Handler (on_click, on_drag, etc.)
    ↓
Circuit Manager (add_component, add_wire, etc.)
    ↓
Canvas Drawing (draw_component, draw_wire, etc.)
    ↓
Visual Update
```
