# Circuit Designer 🔌⚡

## Description

**Circuit Designer** est un outil complet en Python pour créer, éditer et analyser des schémas de circuits électroniques avec une interface graphique intuitive développée avec Tkinter.

![Circuit Designer](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Fonctionnalités

### 🎨 Interface graphique intuitive
- **Canvas principal** pour dessiner et éditer les circuits
- **Palette de composants** avec tous les composants électroniques de base
- **Panneau de propriétés** pour modifier les valeurs en temps réel
- **Barre d'outils** complète avec toutes les actions nécessaires
- **Zone de résultats** affichant les calculs détaillés

### 📦 Composants disponibles
- ⚡ Sources de tension DC
- 🔋 Sources de courant
- 🔲 Résistances
- 🔳 Condensateurs
- 🌀 Inductances
- ➖ Fils de connexion

### 🔬 Moteur de calculs électriques

#### Calculs de base
- **Loi d'Ohm**: V = R × I
- **Puissance**: P = V × I = R × I² = V²/R
- **Résistances équivalentes**:
  - Série: Req = R1 + R2 + ... + Rn
  - Parallèle: 1/Req = 1/R1 + 1/R2 + ... + 1/Rn

#### Théorèmes avancés
- **Diviseur de tension**: Vout = Vin × (R2 / (R1 + R2))
- **Diviseur de courant**: I1 = Itotal × (R2 / (R1 + R2))
- **Théorème de Millman**: Pour calculs de nœuds

### ⚙️ Fonctionnalités supplémentaires
- Détection automatique de la topologie du circuit
- Calcul des tensions aux nœuds
- Calcul des courants dans chaque branche
- Calcul de la puissance dissipée par composant
- Sauvegarde/Chargement en format JSON
- Glisser-déposer des composants
- Grille magnétique (snap-to-grid)

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt**:
```bash
git clone https://github.com/riphaphou/circuit.git
cd circuit
```

2. **Installer les dépendances**:
```bash
pip install -r requirements.txt
```

## Utilisation

### Lancer l'application

```bash
python main.py
```

Ou sur Linux/Mac:
```bash
python3 main.py
```

### Guide d'utilisation rapide

#### 1. Ajouter des composants
1. Cliquez sur un composant dans la palette de gauche
2. Cliquez sur le canvas pour le placer
3. Le composant est ajouté avec ses valeurs par défaut

#### 2. Modifier les propriétés
1. Cliquez droit sur un composant
2. Ses propriétés s'affichent dans le panneau de droite
3. Modifiez le nom, la valeur, etc.
4. Cliquez sur "Appliquer" pour valider

#### 3. Déplacer les composants
1. Cliquez et maintenez sur un composant
2. Glissez-le à la position désirée
3. Relâchez pour le placer

#### 4. Effectuer des calculs
1. Créez votre circuit avec au moins une source et des résistances
2. Cliquez sur le bouton "Calculer" ou pressez F5
3. Les résultats s'affichent dans la zone en bas

#### 5. Sauvegarder/Charger
- **Sauvegarder**: Menu Fichier > Sauvegarder (Ctrl+S)
- **Charger**: Menu Fichier > Ouvrir (Ctrl+O)
- Les circuits sont sauvegardés en format JSON

#### 6. Supprimer un composant
1. Sélectionnez le composant (clic droit)
2. Cliquez sur "Supprimer" dans le panneau de propriétés
3. Ou utilisez Menu Édition > Effacer tout pour tout supprimer

### Raccourcis clavier

| Raccourci | Action |
|-----------|--------|
| Ctrl+N | Nouveau circuit |
| Ctrl+O | Ouvrir un circuit |
| Ctrl+S | Sauvegarder |
| Ctrl+Q | Quitter |
| F5 | Calculer le circuit |

## Structure du projet

```
circuit/
├── main.py                      # Point d'entrée de l'application
├── requirements.txt             # Dépendances Python
├── README.md                    # Ce fichier
├── .gitignore                   # Fichiers à ignorer par Git
├── components/                  # Module des composants électroniques
│   ├── __init__.py
│   ├── base_component.py        # Classe de base pour tous les composants
│   ├── resistor.py             # Résistance
│   ├── voltage_source.py       # Source de tension
│   ├── current_source.py       # Source de courant
│   ├── capacitor.py            # Condensateur
│   ├── inductor.py             # Inductance
│   └── wire.py                 # Fil de connexion
├── circuit/                     # Module de gestion du circuit
│   ├── __init__.py
│   ├── circuit_manager.py      # Gestionnaire de circuit
│   ├── calculator.py           # Moteur de calculs
│   └── analyzer.py             # Analyse de topologie
├── gui/                         # Interface graphique
│   ├── __init__.py
│   ├── main_window.py          # Fenêtre principale
│   ├── canvas.py               # Canvas de dessin
│   ├── component_palette.py   # Palette de composants
│   └── properties_panel.py    # Panneau de propriétés
├── utils/                       # Utilitaires
│   ├── __init__.py
│   └── file_manager.py         # Gestion des fichiers JSON
└── examples/                    # Exemples de circuits
    ├── simple_series.json      # Circuit série simple
    ├── voltage_divider.json    # Diviseur de tension
    └── mixed_components.json   # Circuit avec composants variés
```

## Exemples de circuits

Le dossier `examples/` contient plusieurs circuits d'exemple:

### 1. Circuit série simple (`simple_series.json`)
- 1 source de tension 12V
- 2 résistances en série (1kΩ et 2kΩ)
- Idéal pour comprendre les bases

### 2. Diviseur de tension (`voltage_divider.json`)
- 1 source de 9V
- 2 résistances (4.7kΩ et 2.2kΩ)
- Démontre le diviseur de tension

### 3. Composants mixtes (`mixed_components.json`)
- Source, résistance, condensateur, inductance
- Montre tous les types de composants

Pour ouvrir un exemple:
1. Menu Fichier > Ouvrir
2. Naviguez vers le dossier `examples/`
3. Sélectionnez un fichier `.json`

## Architecture technique

### Conception orientée objet
- **Classe de base `BaseComponent`**: Tous les composants héritent de cette classe
- **Séparation des responsabilités**: GUI, logique métier, et calculs sont séparés
- **Pattern MVC**: Modèle (circuit), Vue (GUI), Contrôleur (gestionnaire)

### Calculs électriques
Le moteur de calcul implémente:
- Loi d'Ohm
- Calculs de puissance
- Résistances équivalentes (série/parallèle)
- Diviseurs de tension et courant
- Théorème de Millman

### Formats de données
- **JSON**: Format de sauvegarde lisible et éditable
- Structure claire avec composants et connexions

## Développement

### Contribuer
Les contributions sont les bienvenues! Pour contribuer:
1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

### Standards de code
- Suivre PEP 8 (style Python)
- Commentaires en français
- Docstrings pour toutes les fonctions
- Noms de variables explicites

### Tests
Pour tester manuellement:
1. Lancez l'application: `python main.py`
2. Testez chaque fonctionnalité
3. Vérifiez les calculs avec des valeurs connues

## Dépannage

### L'application ne se lance pas
- Vérifiez que Python 3.8+ est installé: `python --version`
- Installez les dépendances: `pip install -r requirements.txt`
- Sur Linux, il peut être nécessaire d'installer tk: `sudo apt-get install python3-tk`

### Les calculs sont incorrects
- Vérifiez que toutes les valeurs sont positives
- Assurez-vous qu'il y a au moins une source de tension
- Les résistances ne doivent pas être nulles

### Impossible de sauvegarder
- Vérifiez les permissions du dossier
- Utilisez une extension `.json`

## Limitations actuelles

- Analyse simplifiée (circuits complexes peuvent nécessiter des améliorations)
- Pas de support AC (uniquement DC)
- Connexions entre composants en développement
- Pas d'export d'image pour l'instant

## Améliorations futures

- [ ] Support des circuits AC
- [ ] Analyse fréquentielle
- [ ] Oscilloscope virtuel
- [ ] Export PNG/SVG
- [ ] Composants non-linéaires (diodes, transistors)
- [ ] Simulation temporelle
- [ ] Undo/Redo
- [ ] Copier/Coller de composants

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Auteurs

Développé avec ❤️ pour l'apprentissage de l'électronique

## Support

Pour toute question ou problème:
- Ouvrez une issue sur GitHub
- Consultez la documentation
- Utilisez le menu Aide > Guide d'utilisation dans l'application

---

**Circuit Designer** - Concevez, Analysez, Apprenez 🚀