# Changelog

## Version 1.0.0 - 2026-01-30

### Nouvelles fonctionnalités

#### ✅ Système de connexion de fils
- **Création de fils interactifs**: Cliquez sur un composant pour démarrer un fil, puis cliquez sur un autre composant pour terminer la connexion
- **Feedback visuel en temps réel**: Une ligne pointillée suit la souris lors du traçage
- **Accrochage automatique (snap)**: Les fils s'accrochent automatiquement aux bornes des composants lors du survol
- **Validation**: Impossible de connecter un composant à lui-même
- **Suppression de fils**: Clic droit sur un fil pour le supprimer
- **Gestion des événements Tkinter**:
  - `<Button-1>`: Démarrer/terminer un fil
  - `<B1-Motion>`: Tracer le fil en suivant la souris
  - `<Motion>`: Accrochage automatique aux bornes
  - `<Button-3>`: Menu contextuel pour supprimer

#### ✅ Interface redimensionnable
- **Fenêtre principale redimensionnable**: `root.resizable(True, True)`
- **Layout flexible avec grid**: Tous les widgets s'adaptent automatiquement
- **Taille minimale**: 1000x700 pixels pour une utilisation confortable
- **Canvas extensible**: Le canvas de dessin s'agrandit avec la fenêtre
- **Panneaux flexibles**: Les sections de propriétés et résultats s'adaptent en hauteur

#### ✅ Système de thèmes
Quatre thèmes prédéfinis disponibles via le menu "Apparence":

**1. Thème Clair (par défaut)**
- Fond canvas blanc (#FFFFFF)
- Grille gris clair (#E0E0E0)
- Composants noirs (#000000)
- Interface gris très clair (#F5F5F5)

**2. Thème Sombre**
- Fond canvas gris foncé (#2B2B2B)
- Grille gris moyen (#404040)
- Composants blancs (#FFFFFF)
- Interface noire (#1E1E1E)

**3. Thème Bleu**
- Fond canvas bleu très clair (#E3F2FD)
- Grille bleu clair (#BBDEFB)
- Composants bleu foncé (#1976D2)
- Interface bleu pâle (#F5F9FF)

**4. Thème Vert (mode confort)**
- Fond canvas vert très clair (#E8F5E9)
- Grille vert clair (#C8E6C9)
- Composants vert foncé (#388E3C)
- Interface vert pâle (#F1F8E9)

#### ✅ Image de fond personnalisée
- **Chargement d'images**: Formats supportés PNG, JPG, JPEG, GIF, BMP
- **Modes d'affichage**:
  - Stretch: Ajuste à la taille du canvas
  - Tile: Répète en mosaïque
  - Center: Centre l'image
- **Opacité réglable**: Slider de 0 à 100%
- **Suppression**: Option pour retirer l'image de fond

#### ✅ Persistance des préférences
- Sauvegarde automatique dans `~/.circuit_preferences.json`
- Mémorisation du thème sélectionné
- Mémorisation de l'image de fond et de ses paramètres
- Chargement automatique au démarrage

### Composants disponibles
- **Résistance**: Avec valeur en ohms
- **Pile/Batterie**: Avec tension en volts
- **LED**: Diode électroluminescente
- **Interrupteur**: État ouvert/fermé

### Fonctionnalités de l'application
- **Palette de composants**: Ajout facile de composants au circuit
- **Grille d'alignement**: Grille de 20px pour un placement précis
- **Calculs de circuit**: Calcul de la tension, résistance et courant totaux
- **Panneau de résultats**: Affichage des valeurs calculées
- **Menu contextuel**: Clic droit pour supprimer composants et fils

### Interface utilisateur
- **Barre de menu complète**:
  - Fichier: Nouveau circuit, Quitter
  - Édition: Effacer tout
  - Apparence: Thèmes, Image de fond, Personnaliser
  - Aide: À propos
- **Dialogue de personnalisation**: Fenêtre dédiée pour configurer l'apparence
- **Instructions intégrées**: Guide d'utilisation dans la palette

### Aspects techniques
- **Architecture modulaire**: Séparation claire entre GUI, logique métier et utilitaires
- **Gestion de thèmes centralisée**: `ThemeManager` pour tous les aspects visuels
- **Gestionnaire de circuit**: `CircuitManager` pour la logique des composants et connexions
- **Canvas personnalisé**: `CircuitCanvas` avec gestion avancée des événements
- **Support PIL/Pillow**: Pour le traitement des images de fond

### Dépendances
- Python 3.x
- tkinter (inclus avec Python)
- Pillow >= 10.0.0 (pour les images)

## Notes de version
- Interface fluide et réactive
- Gestion complète des erreurs
- Code documenté en français
- Compatible avec différentes résolutions d'écran
