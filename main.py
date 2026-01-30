#!/usr/bin/env python3
"""
Circuit Designer - Outil de conception de circuits électroniques

Point d'entrée principal de l'application.
"""
import sys
import tkinter as tk
from gui import MainWindow


def main():
    """
    Fonction principale de l'application.
    """
    try:
        # Créer et lancer l'application
        app = MainWindow()
        app.mainloop()
        
    except Exception as e:
        print(f"Erreur lors du lancement de l'application: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
