#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Point d'entrée principal de l'application de conception de circuits électroniques
"""

import tkinter as tk
from gui.main_window import MainWindow

def main():
    """Fonction principale de l'application"""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
