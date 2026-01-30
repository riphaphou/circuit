#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de la mise à jour des pins lors du déplacement de composants
"""

from core.components import Resistor, Battery

def test_pin_updates():
    """Vérifie que les pins se mettent à jour quand on déplace un composant"""
    print("Test de la mise à jour des pins...")
    
    # Créer une résistance
    r = Resistor(100, 100, 1, value=1000)
    
    # Vérifier les pins initiales
    initial_pins = r.pins
    print(f"Position initiale: ({r.x}, {r.y})")
    print(f"Pins initiales: {initial_pins}")
    assert initial_pins == [(60, 100), (140, 100)], "Pins initiales incorrectes"
    
    # Déplacer le composant
    r.x = 200
    r.y = 150
    
    # Vérifier que les pins ont été mises à jour
    updated_pins = r.pins
    print(f"\nPosition déplacée: ({r.x}, {r.y})")
    print(f"Pins mises à jour: {updated_pins}")
    assert updated_pins == [(160, 150), (240, 150)], "Pins non mises à jour"
    
    print("\n✓ Les pins se mettent à jour correctement!")
    
    # Test avec une batterie
    b = Battery(100, 200, 2, voltage=9)
    initial_pins = b.pins
    print(f"\nBatterie position initiale: ({b.x}, {b.y})")
    print(f"Pins initiales: {initial_pins}")
    assert initial_pins == [(100, 170), (100, 230)], "Pins batterie initiales incorrectes"
    
    b.x = 300
    b.y = 250
    updated_pins = b.pins
    print(f"Batterie position déplacée: ({b.x}, {b.y})")
    print(f"Pins mises à jour: {updated_pins}")
    assert updated_pins == [(300, 220), (300, 280)], "Pins batterie non mises à jour"
    
    print("\n✓ Toutes les vérifications sont passées!")
    return True

if __name__ == "__main__":
    test_pin_updates()
