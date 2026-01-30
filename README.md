# Concepteur de Circuits Électroniques

Application de conception et de simulation de circuits électroniques avec interface graphique Tkinter.

## 🎯 Fonctionnalités principales

### ⚡ Conception de circuits
- **Palette de composants**: Résistances, piles, LED, interrupteurs
- **Connexion de fils**: Système intuitif de drag & drop pour connecter les composants
- **Accrochage automatique**: Les fils s'accrochent automatiquement aux bornes des composants
- **Grille d'alignement**: Grille de 20px pour un placement précis
- **Calculs automatiques**: Calcul de la tension, résistance et courant totaux

### 🎨 Personnalisation de l'apparence

#### Thèmes prédéfinis
- **Thème Clair**: Interface lumineuse pour une utilisation en journée
- **Thème Sombre**: Interface sombre pour réduire la fatigue oculaire
- **Thème Bleu**: Couleurs apaisantes pour une utilisation prolongée
- **Thème Vert (confort)**: Mode confort pour les yeux

#### Image de fond
- Support des formats: PNG, JPG, JPEG, GIF, BMP
- Modes d'affichage: Stretch, Tile, Center
- Opacité réglable de 0 à 100%
- Persistance des préférences

### 🖥️ Interface utilisateur
- **Fenêtre redimensionnable**: Interface flexible qui s'adapte à votre écran
- **Taille minimale**: 1000x700 pixels
- **Layout responsive**: Tous les panneaux s'adaptent au redimensionnement
- **Menus contextuels**: Clic droit pour supprimer des éléments

## 📦 Installation

### Prérequis
- Python 3.7 ou supérieur
- tkinter (généralement inclus avec Python)

### Installation des dépendances

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

### Lancement de l'application

```bash
python main.py
```

### Guide d'utilisation

#### Ajouter des composants
1. Cliquez sur un composant dans la palette de gauche
2. Le composant apparaît au centre du canvas
3. Déplacez-le si nécessaire

#### Connecter des fils
1. **Cliquez** sur un composant pour démarrer un fil
2. Une ligne pointillée apparaît et suit votre souris
3. **Cliquez** sur un autre composant pour terminer la connexion
4. Le fil s'accroche automatiquement aux bornes les plus proches

#### Supprimer des éléments
- **Clic droit** sur un fil → Supprime le fil
- **Clic droit** sur un composant → Menu contextuel avec option "Supprimer"

#### Changer de thème
1. Menu **Apparence** → **Thèmes**
2. Sélectionnez un thème dans la liste
3. Le changement est instantané

#### Ajouter une image de fond
1. Menu **Apparence** → **Charger image de fond...**
2. Sélectionnez une image (PNG, JPG, etc.)
3. Réglez l'opacité et le mode d'affichage via **Personnaliser...**

#### Calculer le circuit
1. Ajoutez des composants et connectez-les avec des fils
2. Cliquez sur **Calculer le circuit**
3. Les résultats s'affichent dans le panneau de droite

## 📁 Structure du projet

```
circuit/
├── main.py                    # Point d'entrée de l'application
├── requirements.txt           # Dépendances Python
├── README.md                  # Documentation
├── CHANGELOG.md              # Historique des versions
├── core/                     # Logique métier
│   ├── __init__.py
│   ├── components.py         # Classes des composants (Resistor, Battery, etc.)
│   └── circuit_manager.py    # Gestionnaire de circuit
├── gui/                      # Interface graphique
│   ├── __init__.py
│   ├── main_window.py        # Fenêtre principale
│   ├── canvas.py             # Canvas de dessin
│   └── theme_dialog.py       # Dialogue de personnalisation
└── utils/                    # Utilitaires
    ├── __init__.py
    └── theme_manager.py      # Gestionnaire de thèmes
```

## 🎨 Thèmes disponibles

### Thème Clair
![Thème Clair](#)
- Canvas: Blanc (#FFFFFF)
- Grille: Gris clair (#E0E0E0)
- Composants: Noir (#000000)

### Thème Sombre
![Thème Sombre](#)
- Canvas: Gris foncé (#2B2B2B)
- Grille: Gris moyen (#404040)
- Composants: Blanc (#FFFFFF)

### Thème Bleu
![Thème Bleu](#)
- Canvas: Bleu très clair (#E3F2FD)
- Grille: Bleu clair (#BBDEFB)
- Composants: Bleu foncé (#1976D2)

### Thème Vert
![Thème Vert](#)
- Canvas: Vert très clair (#E8F5E9)
- Grille: Vert clair (#C8E6C9)
- Composants: Vert foncé (#388E3C)

## ⚙️ Fichier de préférences

Les préférences sont sauvegardées automatiquement dans:
```
~/.circuit_preferences.json
```

Contenu:
```json
{
  "theme": "light",
  "background_image": "/path/to/image.png",
  "background_opacity": 100,
  "background_mode": "stretch"
}
```

## 🔧 Développement

### Architecture

L'application suit une architecture MVC (Model-View-Controller):
- **Model**: `core/` - Logique des composants et du circuit
- **View**: `gui/` - Interface graphique Tkinter
- **Controller**: `utils/` - Gestionnaires et utilitaires

### Composants disponibles

#### Résistance (Resistor)
- Valeur par défaut: 1000Ω
- Bornes: Gauche et droite

#### Pile (Battery)
- Tension par défaut: 9V
- Bornes: Haut (+) et bas (-)

#### LED
- Bornes: Gauche et droite
- Représentation: Triangle avec barre

#### Interrupteur (Switch)
- État: Ouvert/Fermé
- Bornes: Gauche et droite

### Ajouter un nouveau composant

1. Créer une classe dans `core/components.py`:
```python
class NewComponent(Component):
    def __init__(self, x, y, component_id):
        super().__init__(x, y, component_id)
        self.pins = [(x-30, y), (x+30, y)]
        
    def draw(self, canvas, theme):
        # Dessiner le composant
        pass
```

2. Ajouter le type dans `CircuitManager.add_component()`
3. Ajouter un bouton dans la palette

## 🐛 Bugs connus et limitations

- Les calculs de circuit sont simplifiés (loi d'Ohm basique)
- Pas de support pour les circuits complexes (résistances en parallèle, etc.)
- Pas de sauvegarde/chargement de circuits

## 📝 TODO / Améliorations futures

- [ ] Sauvegarde et chargement de circuits (format JSON)
- [ ] Calculs avancés (circuits en série/parallèle)
- [ ] Plus de composants (condensateurs, inductances, etc.)
- [ ] Simulation en temps réel
- [ ] Export d'images du circuit
- [ ] Zoom et déplacement du canvas
- [ ] Multiples fils depuis une même borne
- [ ] Étiquettes personnalisées pour les composants

## 📄 Licence

Ce projet est libre d'utilisation pour des fins éducatives et personnelles.

## 👥 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à:
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📞 Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub.

---

**Version**: 1.0.0  
**Date**: 2026-01-30  
**Auteur**: Circuit Design Team