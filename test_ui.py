#!/usr/bin/env python3
"""
Script de test simple pour valider l'interface graphique.
"""
import sys
import tkinter as tk
from gui.main_window import MainWindow

def test_basic_ui():
    """Test basique de l'interface."""
    print("Démarrage du test de l'interface...")
    
    # Créer la fenêtre principale
    try:
        app = MainWindow()
        print("✓ Fenêtre principale créée avec succès")
        
        # Vérifier que le canvas existe et peut s'étendre
        assert hasattr(app, 'canvas'), "Le canvas n'existe pas"
        print("✓ Canvas créé avec succès")
        
        # Vérifier que la palette existe
        assert hasattr(app, 'palette'), "La palette n'existe pas"
        print("✓ Palette créée avec succès")
        
        # Vérifier que le panneau de propriétés existe
        assert hasattr(app, 'properties'), "Le panneau de propriétés n'existe pas"
        print("✓ Panneau de propriétés créé avec succès")
        
        # Vérifier que la zone de résultats existe
        assert hasattr(app, 'results_text'), "La zone de résultats n'existe pas"
        print("✓ Zone de résultats créée avec succès")
        
        # Vérifier que le canvas a la méthode set_component_to_place
        assert hasattr(app.canvas, 'set_component_to_place'), "La méthode set_component_to_place n'existe pas"
        print("✓ Méthode de placement de composants disponible")
        
        # Test de la méthode de placement
        from components import Resistor
        app.canvas.set_component_to_place(Resistor)
        assert app.canvas.component_to_place == Resistor, "Le composant à placer n'a pas été défini correctement"
        assert app.canvas.cget('cursor') == 'crosshair', "Le curseur n'a pas changé"
        print("✓ Test de sélection de composant réussi")
        
        print("\n✅ Tous les tests de base sont passés!")
        print("\nVous pouvez maintenant tester manuellement:")
        print("1. Redimensionner la fenêtre pour vérifier la réactivité")
        print("2. Cliquer sur 'Résistance' puis sur le canvas pour placer un composant")
        print("3. Essayer de déplacer un composant")
        print("\nAppuyez sur Ctrl+Q ou fermez la fenêtre pour quitter.")
        
        # Lancer l'application
        app.mainloop()
        
    except Exception as e:
        print(f"✗ Erreur lors du test: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = test_basic_ui()
    sys.exit(0 if success else 1)
