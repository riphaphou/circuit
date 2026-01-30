#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de vérification visuelle (nécessite un serveur X)
Ce script tente de créer l'interface et de prendre une capture d'écran
"""

import sys
import os

def test_visual_app():
    """Teste l'application avec interface graphique"""
    try:
        import tkinter as tk
        from gui.main_window import MainWindow
        
        print("Création de l'interface graphique...")
        root = tk.Tk()
        app = MainWindow(root)
        
        # Ajouter quelques composants pour la démo
        print("Ajout de composants de démonstration...")
        app.add_component('battery')
        app.circuit_manager.components[1].x = 300
        app.circuit_manager.components[1].y = 200
        
        app.add_component('resistor')
        app.circuit_manager.components[2].x = 450
        app.circuit_manager.components[2].y = 200
        
        app.add_component('led')
        app.circuit_manager.components[3].x = 600
        app.circuit_manager.components[3].y = 200
        
        # Connecter les composants
        print("Création de connexions...")
        b1 = app.circuit_manager.components[1]
        r1 = app.circuit_manager.components[2]
        led1 = app.circuit_manager.components[3]
        
        app.circuit_manager.add_wire(b1.id, b1.pins[0], r1.id, r1.pins[0])
        app.circuit_manager.add_wire(r1.id, r1.pins[1], led1.id, led1.pins[0])
        app.circuit_manager.add_wire(led1.id, led1.pins[1], b1.id, b1.pins[1])
        
        # Redessiner
        app.canvas.redraw()
        
        # Calculer
        app.calculate_circuit()
        
        print("Interface créée avec succès!")
        print("\nPour tester visuellement:")
        print("1. Lancez: python main.py")
        print("2. Testez les fonctionnalités interactives")
        print("3. Vérifiez les thèmes dans le menu Apparence")
        
        # Essayer de prendre une capture d'écran
        try:
            root.update()
            print("\nTentative de capture d'écran...")
            # Note: Nécessite un serveur X actif
            print("(Capture d'écran ignorée - pas de serveur X)")
        except Exception as e:
            print(f"Capture impossible: {e}")
        
        # Ne pas exécuter mainloop dans le test
        root.destroy()
        return True
        
    except ImportError as e:
        print(f"Module manquant: {e}")
        print("L'interface graphique nécessite tkinter.")
        print("Sur Ubuntu/Debian: sudo apt-get install python3-tk")
        return False
    except Exception as e:
        print(f"Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Test de l'interface graphique")
    print("=" * 60)
    print()
    
    success = test_visual_app()
    
    print()
    print("=" * 60)
    if success:
        print("✓ Test réussi!")
    else:
        print("✗ Test échoué")
    print("=" * 60)
