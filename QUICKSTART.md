# Guide de Démarrage Rapide - Circuit Designer

## Installation Express

```bash
# 1. Cloner le dépôt
git clone https://github.com/riphaphou/circuit.git
cd circuit

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Sur Linux uniquement: installer python3-tk
sudo apt-get install python3-tk  # Ubuntu/Debian
sudo yum install python3-tkinter  # CentOS/RHEL

# 4. Lancer l'application
python main.py
```

## Premiers Pas

### 1. Créer votre premier circuit

1. **Lancez l'application**: `python main.py`
2. **Ajoutez une source de tension**:
   - Cliquez sur "Source de Tension" dans la palette
   - Cliquez sur le canvas pour la placer
3. **Ajoutez une résistance**:
   - Cliquez sur "Résistance"
   - Cliquez sur le canvas
4. **Modifier les valeurs**:
   - Clic droit sur un composant
   - Modifiez la valeur dans le panneau de droite
   - Cliquez "Appliquer"
5. **Calculer**:
   - Cliquez sur le bouton "Calculer" ou F5
   - Les résultats s'affichent en bas

### 2. Charger un exemple

1. Menu **Fichier** > **Ouvrir**
2. Naviguez vers le dossier `examples/`
3. Choisissez un fichier (ex: `simple_series.json`)
4. Cliquez "Calculer" pour voir les résultats

### 3. Sauvegarder votre travail

1. Menu **Fichier** > **Sauvegarder sous...**
2. Choisissez un nom et un emplacement
3. Format JSON automatique

## Exemples de Circuits

### Circuit 1: Série Simple
**Fichier**: `examples/simple_series.json`
- Source: 12V
- Résistances: 1kΩ + 2kΩ
- **Résultats attendus**:
  - Courant: 4 mA
  - Req: 3 kΩ

### Circuit 2: Diviseur de Tension
**Fichier**: `examples/voltage_divider.json`
- Source: 9V
- R1: 4.7kΩ
- R2: 2.2kΩ
- **Résultats attendus**:
  - Vout ≈ 2.87V (sur R2)

### Circuit 3: Composants Mixtes
**Fichier**: `examples/mixed_components.json`
- Démontre tous les types de composants

## Raccourcis Utiles

| Touche | Action |
|--------|--------|
| **Ctrl+N** | Nouveau circuit |
| **Ctrl+O** | Ouvrir |
| **Ctrl+S** | Sauvegarder |
| **F5** | Calculer |
| **Ctrl+Q** | Quitter |

## Composants Disponibles

| Composant | Symbole | Unité | Valeur par défaut |
|-----------|---------|-------|-------------------|
| Résistance | R | Ω | 1 kΩ |
| Source de Tension | V | V | 12 V |
| Source de Courant | I | A | 1 mA |
| Condensateur | C | F | 1 µF |
| Inductance | L | H | 1 mH |
| Fil | W | - | - |

## Astuces

### ✨ Pour un circuit parfait
1. Placez la source de tension en premier
2. Ajoutez les résistances ensuite
3. Utilisez la grille pour aligner les composants
4. Nommez vos composants de manière logique (R1, R2, etc.)

### 📐 Calculs précis
- Vérifiez que toutes les valeurs sont positives
- Au moins une source est nécessaire
- Les résistances ne peuvent pas être nulles
- Le circuit doit être fermé pour les calculs

### 💾 Organisation
- Sauvegardez régulièrement votre travail
- Utilisez des noms descriptifs pour vos fichiers
- Créez un dossier pour vos projets

## Dépannage Rapide

### L'application ne démarre pas
```bash
# Vérifier Python
python --version  # Doit être 3.8+

# Installer les dépendances
pip install -r requirements.txt

# Sur Linux, installer tk
sudo apt-get install python3-tk
```

### Les calculs semblent incorrects
- Vérifiez les valeurs des composants
- Assurez-vous qu'il y a une source
- Les résistances doivent être > 0

### Impossible de sauvegarder
- Vérifiez les permissions du dossier
- Utilisez l'extension `.json`

## Prochaines Étapes

1. **Explorez les exemples** dans le dossier `examples/`
2. **Créez vos propres circuits** pas à pas
3. **Expérimentez** avec différentes valeurs
4. **Consultez le README.md** pour plus de détails

## Support

- 📖 Documentation complète: `README.md`
- 🧪 Résultats des tests: `TESTS.md`
- ❓ Menu Aide > Guide d'utilisation (dans l'app)
- 🐛 Issues: https://github.com/riphaphou/circuit/issues

---

**Bon circuit! ⚡🔌**
