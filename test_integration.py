#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test d'intégration de l'interface graphique
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_gui_creation():
    """Test de création de l'interface sans l'afficher"""
    print("Test de création de l'interface...")
    
    import tkinter as tk
    from gui.main_window import MainWindow
    
    try:
        # Créer la fenêtre sans l'afficher
        root = tk.Tk()
        root.withdraw()  # Ne pas afficher la fenêtre
        
        # Créer l'application
        app = MainWindow(root)
        
        # Vérifier que les composants sont créés
        assert hasattr(app, 'circuit_manager'), "CircuitManager manquant"
        assert hasattr(app, 'theme_manager'), "ThemeManager manquant"
        assert hasattr(app, 'canvas'), "Canvas manquant"
        
        # Test ajout de composants
        app.add_component('resistor')
        assert len(app.circuit_manager.components) == 1, "Composant non ajouté"
        
        app.add_component('battery')
        assert len(app.circuit_manager.components) == 2, "Deuxième composant non ajouté"
        
        # Test changement de thème
        app.apply_theme_by_id('dark')
        assert app.theme_manager.current_theme == 'dark', "Thème non changé"
        
        app.apply_theme_by_id('blue')
        assert app.theme_manager.current_theme == 'blue', "Thème bleu non appliqué"
        
        # Test calcul
        results = app.circuit_manager.calculate_circuit()
        assert 'voltage' in results, "Résultats de calcul manquants"
        
        # Test effacer circuit
        app.clear_circuit()
        assert len(app.circuit_manager.components) == 0, "Circuit non effacé"
        
        root.destroy()
        
        print("✓ Interface graphique créée et fonctionnelle")
        return True
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_wire_connections():
    """Test des connexions de fils"""
    print("\nTest des connexions de fils...")
    
    from core.circuit_manager import CircuitManager
    
    manager = CircuitManager()
    
    # Ajouter des composants
    r1 = manager.add_component('resistor', 100, 100)
    r2 = manager.add_component('resistor', 200, 100)
    b1 = manager.add_component('battery', 150, 200)
    
    # Connecter avec des fils
    w1 = manager.add_wire(r1.id, r1.pins[1], b1.id, b1.pins[0])
    assert w1 is not None, "Fil 1 non créé"
    
    w2 = manager.add_wire(r2.id, r2.pins[0], b1.id, b1.pins[1])
    assert w2 is not None, "Fil 2 non créé"
    
    # Tenter une connexion invalide (composant à lui-même)
    w_invalid = manager.add_wire(r1.id, r1.pins[0], r1.id, r1.pins[1])
    assert w_invalid is None, "Validation échouée: connexion à soi-même acceptée"
    
    # Vérifier le nombre de fils
    assert len(manager.wires) == 2, "Nombre de fils incorrect"
    
    # Test suppression de fil
    manager.remove_wire(w1.id)
    assert len(manager.wires) == 1, "Fil non supprimé"
    
    # Test suppression de composant (doit supprimer les fils associés)
    manager.remove_component(b1.id)
    assert len(manager.wires) == 0, "Fils non supprimés avec le composant"
    
    print("✓ Connexions de fils fonctionnelles")
    return True

def test_themes():
    """Test des thèmes"""
    print("\nTest des thèmes...")
    
    from utils.theme_manager import ThemeManager
    
    manager = ThemeManager()
    
    # Tester tous les thèmes
    themes_to_test = ['light', 'dark', 'blue', 'green']
    
    for theme_name in themes_to_test:
        manager.apply_theme(theme_name)
        theme = manager.get_current_theme()
        
        # Vérifier les clés requises
        required_keys = ['canvas_bg', 'grid_color', 'component_color', 
                        'text_color', 'wire_color', 'ui_bg']
        for key in required_keys:
            assert key in theme, f"Clé {key} manquante dans thème {theme_name}"
        
        print(f"  ✓ Thème {theme_name} : OK")
    
    print("✓ Tous les thèmes fonctionnels")
    return True

def test_resizable_layout():
    """Test du layout redimensionnable"""
    print("\nTest du layout redimensionnable...")
    
    import tkinter as tk
    from gui.main_window import MainWindow
    
    try:
        root = tk.Tk()
        root.withdraw()
        
        app = MainWindow(root)
        
        # Vérifier que la fenêtre est redimensionnable
        assert root.resizable()[0] == True, "Fenêtre non redimensionnable en largeur"
        assert root.resizable()[1] == True, "Fenêtre non redimensionnable en hauteur"
        
        # Vérifier la taille minimale
        min_width = root.minsize()[0]
        min_height = root.minsize()[1]
        assert min_width >= 1000, f"Largeur minimale trop petite: {min_width}"
        assert min_height >= 700, f"Hauteur minimale trop petite: {min_height}"
        
        root.destroy()
        
        print("✓ Layout redimensionnable configuré correctement")
        return True
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Tests d'intégration de l'application")
    print("=" * 60)
    
    tests = [
        test_gui_creation,
        test_wire_connections,
        test_themes,
        test_resizable_layout,
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
    
    sys.exit(0 if failed == 0 else 1)
