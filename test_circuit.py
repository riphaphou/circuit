#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests de base pour l'application de circuits
"""

import sys
import os

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test que tous les modules peuvent être importés"""
    print("Test des imports...")
    try:
        from core.components import Component, Resistor, Battery, LED, Switch, Wire
        from core.circuit_manager import CircuitManager
        from utils.theme_manager import ThemeManager
        print("✓ Tous les modules importés avec succès")
        return True
    except ImportError as e:
        print(f"✗ Erreur d'import: {e}")
        return False

def test_circuit_manager():
    """Test du gestionnaire de circuit"""
    print("\nTest du CircuitManager...")
    from core.circuit_manager import CircuitManager
    
    manager = CircuitManager()
    
    # Test ajout de composants
    r1 = manager.add_component("resistor", 100, 100, value=1000)
    assert r1 is not None, "Échec ajout résistance"
    assert r1.value == 1000, "Valeur résistance incorrecte"
    
    b1 = manager.add_component("battery", 200, 100, voltage=9)
    assert b1 is not None, "Échec ajout batterie"
    assert b1.voltage == 9, "Tension batterie incorrecte"
    
    # Test connexion de fils
    wire = manager.add_wire(r1.id, r1.pins[0], b1.id, b1.pins[0])
    assert wire is not None, "Échec création fil"
    
    # Test validation (pas de connexion à soi-même)
    invalid_wire = manager.add_wire(r1.id, r1.pins[0], r1.id, r1.pins[1])
    assert invalid_wire is None, "Validation fil échouée"
    
    # Test suppression
    manager.remove_component(r1.id)
    assert r1.id not in manager.components, "Échec suppression composant"
    assert wire.id not in manager.wires, "Fils non supprimés avec le composant"
    
    print("✓ CircuitManager fonctionne correctement")
    return True

def test_theme_manager():
    """Test du gestionnaire de thèmes"""
    print("\nTest du ThemeManager...")
    from utils.theme_manager import ThemeManager
    
    manager = ThemeManager()
    
    # Test thèmes
    assert 'light' in manager.THEMES, "Thème light manquant"
    assert 'dark' in manager.THEMES, "Thème dark manquant"
    assert 'blue' in manager.THEMES, "Thème blue manquant"
    assert 'green' in manager.THEMES, "Thème green manquant"
    
    # Test changement de thème
    result = manager.apply_theme('dark')
    assert result == True, "Échec application thème dark"
    assert manager.current_theme == 'dark', "Thème non changé"
    
    theme = manager.get_current_theme()
    assert 'canvas_bg' in theme, "Clé canvas_bg manquante"
    assert 'component_color' in theme, "Clé component_color manquante"
    
    print("✓ ThemeManager fonctionne correctement")
    return True

def test_components():
    """Test des composants"""
    print("\nTest des composants...")
    from core.components import Resistor, Battery, LED, Switch
    
    # Test résistance
    r = Resistor(100, 100, 1, value=2200)
    assert r.value == 2200, "Valeur résistance incorrecte"
    assert len(r.pins) == 2, "Nombre de pins incorrect pour résistance"
    
    # Test batterie
    b = Battery(200, 200, 2, voltage=12)
    assert b.voltage == 12, "Tension batterie incorrecte"
    assert len(b.pins) == 2, "Nombre de pins incorrect pour batterie"
    
    # Test LED
    led = LED(300, 300, 3)
    assert len(led.pins) == 2, "Nombre de pins incorrect pour LED"
    
    # Test interrupteur
    sw = Switch(400, 400, 4, closed=False)
    assert sw.closed == False, "État interrupteur incorrect"
    assert len(sw.pins) == 2, "Nombre de pins incorrect pour interrupteur"
    
    print("✓ Tous les composants fonctionnent correctement")
    return True

def run_all_tests():
    """Exécute tous les tests"""
    print("=" * 60)
    print("Tests de l'application de circuits électroniques")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_circuit_manager,
        test_theme_manager,
        test_components,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ Exception dans {test.__name__}: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Résultats: {passed} réussis, {failed} échoués")
    print("=" * 60)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
