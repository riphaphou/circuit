"""
Panneau de propriétés pour éditer les composants.
"""
import tkinter as tk
from tkinter import ttk, messagebox


class PropertiesPanel(ttk.Frame):
    """Panneau pour éditer les propriétés des composants."""
    
    def __init__(self, master, canvas, **kwargs):
        """
        Initialise le panneau.
        
        Args:
            master: Widget parent
            canvas: CircuitCanvas contenant les composants
            **kwargs: Arguments pour ttk.Frame
        """
        super().__init__(master, **kwargs)
        self.canvas = canvas
        self.current_component = None
        
        # Titre
        title = ttk.Label(self, text="Propriétés", font=("Arial", 12, "bold"))
        title.pack(pady=5)
        
        # Champs d'édition
        self.create_property_fields()
        
        # Boutons
        self.create_buttons()
        
        # Écouter les événements de sélection
        self.canvas.bind("<<ComponentSelected>>", self.on_component_selected)
    
    def create_property_fields(self):
        """Crée les champs d'édition des propriétés."""
        # Frame pour les champs
        fields_frame = ttk.Frame(self)
        fields_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Nom du composant
        ttk.Label(fields_frame, text="Composant:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(fields_frame, textvariable=self.name_var, width=15)
        self.name_entry.grid(row=0, column=1, pady=5)
        
        # Type
        ttk.Label(fields_frame, text="Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.type_var = tk.StringVar()
        self.type_label = ttk.Label(fields_frame, textvariable=self.type_var)
        self.type_label.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Valeur
        ttk.Label(fields_frame, text="Valeur:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.value_var = tk.StringVar()
        self.value_entry = ttk.Entry(fields_frame, textvariable=self.value_var, width=15)
        self.value_entry.grid(row=2, column=1, pady=5)
        
        # Unité
        ttk.Label(fields_frame, text="Unité:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.unit_var = tk.StringVar()
        self.unit_label = ttk.Label(fields_frame, textvariable=self.unit_var)
        self.unit_label.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Position
        ttk.Label(fields_frame, text="Position X:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.x_var = tk.StringVar()
        self.x_label = ttk.Label(fields_frame, textvariable=self.x_var)
        self.x_label.grid(row=4, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(fields_frame, text="Position Y:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.y_var = tk.StringVar()
        self.y_label = ttk.Label(fields_frame, textvariable=self.y_var)
        self.y_label.grid(row=5, column=1, sticky=tk.W, pady=5)
    
    def create_buttons(self):
        """Crée les boutons d'action."""
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        
        # Bouton Appliquer
        apply_btn = ttk.Button(btn_frame, text="Appliquer", command=self.apply_changes)
        apply_btn.pack(side=tk.LEFT, padx=5)
        
        # Bouton Supprimer
        delete_btn = ttk.Button(btn_frame, text="Supprimer", command=self.delete_component)
        delete_btn.pack(side=tk.LEFT, padx=5)
    
    def on_component_selected(self, event=None):
        """Appelé quand un composant est sélectionné."""
        if self.canvas.selected_component:
            self.load_component(self.canvas.selected_component)
    
    def load_component(self, component):
        """
        Charge les propriétés d'un composant dans le panneau.
        
        Args:
            component: Composant à charger
        """
        self.current_component = component
        
        # Remplir les champs
        self.name_var.set(component.name)
        self.type_var.set(component.get_symbol_name())
        self.value_var.set(str(component.value))
        self.unit_var.set(component.get_unit())
        self.x_var.set(str(component.x))
        self.y_var.set(str(component.y))
    
    def apply_changes(self):
        """Applique les modifications aux propriétés du composant."""
        if not self.current_component:
            messagebox.showwarning("Attention", "Aucun composant sélectionné")
            return
        
        try:
            # Mettre à jour le nom
            new_name = self.name_var.get()
            if new_name:
                self.current_component.name = new_name
            
            # Mettre à jour la valeur
            new_value = float(self.value_var.get())
            self.current_component.value = new_value
            
            # Redessiner le composant
            self.canvas.draw_component(self.current_component)
            
            messagebox.showinfo("Succès", "Propriétés mises à jour")
            
        except ValueError:
            messagebox.showerror("Erreur", "Valeur invalide")
    
    def delete_component(self):
        """Supprime le composant sélectionné."""
        if not self.current_component:
            messagebox.showwarning("Attention", "Aucun composant sélectionné")
            return
        
        # Demander confirmation
        if messagebox.askyesno("Confirmation", 
                              f"Supprimer {self.current_component.name} ?"):
            # Supprimer du gestionnaire
            self.canvas.circuit_manager.remove_component(self.current_component)
            
            # Redessiner le canvas
            self.canvas.redraw_all()
            
            # Effacer les champs
            self.clear_fields()
            
            self.current_component = None
    
    def clear_fields(self):
        """Efface tous les champs."""
        self.name_var.set("")
        self.type_var.set("")
        self.value_var.set("")
        self.unit_var.set("")
        self.x_var.set("")
        self.y_var.set("")
