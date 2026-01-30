#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemple d'utilisation de l'application de circuits
"""

def example_simple_circuit():
    """Exemple de création d'un circuit simple"""
    from core.circuit_manager import CircuitManager
    
    print("=" * 60)
    print("Exemple: Circuit simple avec résistance et pile")
    print("=" * 60)
    
    # Créer un gestionnaire de circuit
    manager = CircuitManager()
    
    # Ajouter des composants
    print("\n1. Ajout des composants:")
    resistor = manager.add_component('resistor', 100, 100, value=220)
    print(f"   ✓ Résistance: {resistor.value}Ω à position ({resistor.x}, {resistor.y})")
    
    battery = manager.add_component('battery', 200, 200, voltage=9)
    print(f"   ✓ Pile: {battery.voltage}V à position ({battery.x}, {battery.y})")
    
    led = manager.add_component('led', 300, 100)
    print(f"   ✓ LED à position ({led.x}, {led.y})")
    
    # Connecter les composants
    print("\n2. Connexion des fils:")
    wire1 = manager.add_wire(resistor.id, resistor.pins[1], battery.id, battery.pins[0])
    print(f"   ✓ Fil {wire1.id}: Résistance → Pile (borne +)")
    
    wire2 = manager.add_wire(led.id, led.pins[0], resistor.id, resistor.pins[0])
    print(f"   ✓ Fil {wire2.id}: LED → Résistance")
    
    wire3 = manager.add_wire(battery.id, battery.pins[1], led.id, led.pins[1])
    print(f"   ✓ Fil {wire3.id}: Pile (borne -) → LED")
    
    # Calculer le circuit
    print("\n3. Calculs du circuit:")
    results = manager.calculate_circuit()
    print(f"   Tension totale: {results['voltage']:.2f} V")
    print(f"   Résistance totale: {results['total_resistance']:.2f} Ω")
    print(f"   Courant: {results['current']*1000:.2f} mA")
    
    print("\n4. État final du circuit:")
    print(f"   Composants: {len(manager.components)}")
    print(f"   Fils: {len(manager.wires)}")
    
    return manager

def example_theme_switching():
    """Exemple de changement de thèmes"""
    from utils.theme_manager import ThemeManager
    
    print("\n" + "=" * 60)
    print("Exemple: Changement de thèmes")
    print("=" * 60)
    
    manager = ThemeManager()
    
    for theme_id, theme_name in manager.get_theme_names():
        manager.apply_theme(theme_id)
        theme = manager.get_current_theme()
        
        print(f"\nThème: {theme_name}")
        print(f"  Canvas: {theme['canvas_bg']}")
        print(f"  Grille: {theme['grid_color']}")
        print(f"  Composants: {theme['component_color']}")
        print(f"  Texte: {theme['text_color']}")
        print(f"  Fils: {theme['wire_color']}")

def example_wire_validation():
    """Exemple de validation des fils"""
    from core.circuit_manager import CircuitManager
    
    print("\n" + "=" * 60)
    print("Exemple: Validation des connexions")
    print("=" * 60)
    
    manager = CircuitManager()
    
    r1 = manager.add_component('resistor', 100, 100)
    r2 = manager.add_component('resistor', 200, 100)
    
    print("\n1. Connexion valide (entre deux composants différents):")
    wire = manager.add_wire(r1.id, r1.pins[0], r2.id, r2.pins[1])
    if wire:
        print(f"   ✓ Fil créé avec succès (ID: {wire.id})")
    else:
        print("   ✗ Échec de création du fil")
    
    print("\n2. Connexion invalide (composant connecté à lui-même):")
    invalid_wire = manager.add_wire(r1.id, r1.pins[0], r1.id, r1.pins[1])
    if invalid_wire is None:
        print("   ✓ Connexion refusée (validation OK)")
    else:
        print("   ✗ Connexion acceptée (erreur de validation)")

def example_component_removal():
    """Exemple de suppression de composants"""
    from core.circuit_manager import CircuitManager
    
    print("\n" + "=" * 60)
    print("Exemple: Suppression de composants et fils associés")
    print("=" * 60)
    
    manager = CircuitManager()
    
    # Créer un circuit
    r1 = manager.add_component('resistor', 100, 100)
    r2 = manager.add_component('resistor', 200, 100)
    b1 = manager.add_component('battery', 150, 200)
    
    w1 = manager.add_wire(r1.id, r1.pins[1], b1.id, b1.pins[0])
    w2 = manager.add_wire(r2.id, r2.pins[0], b1.id, b1.pins[1])
    
    print(f"\nÉtat initial:")
    print(f"  Composants: {len(manager.components)}")
    print(f"  Fils: {len(manager.wires)}")
    
    print(f"\nSuppression de la batterie (ID: {b1.id})...")
    manager.remove_component(b1.id)
    
    print(f"\nÉtat après suppression:")
    print(f"  Composants: {len(manager.components)}")
    print(f"  Fils: {len(manager.wires)} (fils connectés supprimés automatiquement)")

def show_usage_instructions():
    """Affiche les instructions d'utilisation"""
    print("\n" + "=" * 60)
    print("Instructions d'utilisation de l'application")
    print("=" * 60)
    
    print("""
Pour lancer l'application graphique:

    python main.py

Fonctionnalités disponibles:

1. AJOUT DE COMPOSANTS
   - Cliquez sur un bouton dans la palette de gauche
   - Le composant apparaît au centre du canvas

2. CONNEXION DE FILS
   - Cliquez sur un composant pour démarrer un fil
   - Une ligne pointillée suit votre souris
   - Cliquez sur un autre composant pour terminer
   - Le fil s'accroche automatiquement aux bornes

3. SUPPRESSION
   - Clic droit sur un fil → Supprime le fil
   - Clic droit sur un composant → Menu avec option Supprimer

4. CHANGEMENT DE THÈME
   - Menu Apparence → Thèmes
   - Choisir parmi: Clair, Sombre, Bleu, Vert

5. IMAGE DE FOND
   - Menu Apparence → Charger image de fond
   - Formats: PNG, JPG, JPEG, GIF, BMP
   - Personnaliser l'opacité et le mode d'affichage

6. CALCULS
   - Bouton "Calculer le circuit"
   - Affiche tension, résistance et courant totaux

7. REDIMENSIONNEMENT
   - La fenêtre est entièrement redimensionnable
   - Tous les panneaux s'adaptent automatiquement
    """)

if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "EXEMPLES D'UTILISATION DE L'APPLICATION" + " " * 8 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Exécuter tous les exemples
    example_simple_circuit()
    example_theme_switching()
    example_wire_validation()
    example_component_removal()
    show_usage_instructions()
    
    print("\n" + "=" * 60)
    print("Tous les exemples ont été exécutés avec succès!")
    print("=" * 60 + "\n")
