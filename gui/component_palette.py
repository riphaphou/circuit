"""
Palette de composants pour sélection.
"""
import tkinter as tk
from tkinter import ttk


class ComponentPalette(ttk.Frame):
    """Palette de sélection des composants."""
    
    def __init__(self, master, canvas, **kwargs):
        """
        Initialise la palette.
        
        Args:
            master: Widget parent
            canvas: CircuitCanvas pour ajouter les composants
            **kwargs: Arguments pour ttk.Frame
        """
        super().__init__(master, **kwargs)
        self.canvas = canvas
        
        # Titre
        title = ttk.Label(self, text="Composants", font=("Arial", 12, "bold"))
        title.pack(pady=5)
        
        # Boutons pour chaque type de composant
        self.create_component_button("Résistance", "Resistor", "#FFE4B5")
        self.create_component_button("Source de Tension", "VoltageSource", "#FFB6C1")
        self.create_component_button("Source de Courant", "CurrentSource", "#B0E0E6")
        self.create_component_button("Condensateur", "Capacitor", "#DDA0DD")
        self.create_component_button("Inductance", "Inductor", "#98FB98")
        self.create_component_button("Fil", "Wire", "#D3D3D3")
        
        # Séparateur
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Informations
        info_label = ttk.Label(self, text="Cliquez sur un composant\npuis sur le canvas\npour l'ajouter", 
                              justify=tk.LEFT, font=("Arial", 9))
        info_label.pack(pady=5)
        
        # Variable pour stocker le type de composant sélectionné
        self.selected_component_type = None
    
    def create_component_button(self, text, comp_type, color):
        """
        Crée un bouton pour un type de composant.
        
        Args:
            text: Texte du bouton
            comp_type: Type de composant
            color: Couleur du bouton
        """
        btn = tk.Button(
            self,
            text=text,
            bg=color,
            relief=tk.RAISED,
            command=lambda: self.select_component(comp_type),
            width=15,
            height=2,
            font=("Arial", 10)
        )
        btn.pack(pady=3, padx=5, fill=tk.X)
    
    def select_component(self, comp_type):
        """
        Sélectionne un type de composant.
        
        Args:
            comp_type: Type de composant à sélectionner
        """
        from components import Resistor, VoltageSource, CurrentSource, Capacitor, Inductor, Wire
        
        # Mapper les types
        type_map = {
            'Resistor': Resistor,
            'VoltageSource': VoltageSource,
            'CurrentSource': CurrentSource,
            'Capacitor': Capacitor,
            'Inductor': Inductor,
            'Wire': Wire
        }
        
        component_class = type_map.get(comp_type)
        
        if component_class:
            # Dire au canvas quel composant placer au prochain clic
            self.canvas.set_component_to_place(component_class)
