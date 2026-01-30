# -*- coding: utf-8 -*-
"""
Fenêtre principale de l'application
"""

import tkinter as tk
from tkinter import ttk, messagebox
from core.circuit_manager import CircuitManager
from utils.theme_manager import ThemeManager
from gui.canvas import CircuitCanvas
from gui.theme_dialog import ThemeDialog

class MainWindow:
    """Fenêtre principale de l'application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Concepteur de Circuits Électroniques")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Activer le redimensionnement
        self.root.resizable(True, True)
        
        # Initialiser les gestionnaires
        self.circuit_manager = CircuitManager()
        self.theme_manager = ThemeManager()
        
        # Créer l'interface
        self.create_menu()
        self.create_widgets()
        
        # Appliquer le thème initial
        self.apply_theme()
        
        # Configurer le redimensionnement
        self.configure_grid_weights()
        
    def create_menu(self):
        """Crée la barre de menu"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Fichier
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Nouveau circuit", command=self.new_circuit)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.root.quit)
        
        # Menu Édition
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Édition", menu=edit_menu)
        edit_menu.add_command(label="Effacer tout", command=self.clear_circuit)
        
        # Menu Apparence
        appearance_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Apparence", menu=appearance_menu)
        
        # Sous-menu Thèmes
        theme_menu = tk.Menu(appearance_menu, tearoff=0)
        appearance_menu.add_cascade(label="Thèmes", menu=theme_menu)
        
        for theme_id, theme_name in self.theme_manager.get_theme_names():
            theme_menu.add_command(
                label=theme_name,
                command=lambda t=theme_id: self.apply_theme_by_id(t)
            )
            
        appearance_menu.add_separator()
        appearance_menu.add_command(label="Charger image de fond...", 
                                   command=self.load_background_image)
        appearance_menu.add_command(label="Supprimer image de fond", 
                                   command=self.remove_background_image)
        appearance_menu.add_separator()
        appearance_menu.add_command(label="Personnaliser...", 
                                   command=self.open_theme_dialog)
        
        # Menu Aide
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="À propos", command=self.show_about)
        
    def create_widgets(self):
        """Crée les widgets de l'interface"""
        # Frame principal avec grid
        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, sticky='nsew')
        
        # Frame gauche - Palette de composants
        self.palette_frame = ttk.LabelFrame(main_frame, text="Composants", 
                                           padding=10)
        self.palette_frame.grid(row=0, column=0, sticky='ns', padx=5, pady=5)
        
        self.create_component_palette()
        
        # Frame central - Canvas
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.canvas = CircuitCanvas(canvas_frame, self.circuit_manager, 
                                   self.theme_manager, bg='white')
        self.canvas.pack(fill='both', expand=True)
        
        # Frame droit - Propriétés et résultats
        right_frame = ttk.Frame(main_frame)
        right_frame.grid(row=0, column=2, sticky='ns', padx=5, pady=5)
        
        # Propriétés
        self.properties_frame = ttk.LabelFrame(right_frame, text="Propriétés", 
                                              padding=10)
        self.properties_frame.pack(fill='both', expand=True, pady=(0, 5))
        
        ttk.Label(self.properties_frame, 
                 text="Sélectionnez un composant\npour voir ses propriétés",
                 justify='center').pack(pady=20)
        
        # Résultats
        self.results_frame = ttk.LabelFrame(right_frame, text="Calculs", 
                                           padding=10)
        self.results_frame.pack(fill='both', expand=True, pady=(5, 0))
        
        self.results_text = tk.Text(self.results_frame, height=10, width=25, 
                                   wrap='word', state='disabled')
        self.results_text.pack(fill='both', expand=True)
        
        # Bouton calculer
        ttk.Button(right_frame, text="Calculer le circuit", 
                  command=self.calculate_circuit).pack(fill='x', pady=5)
                  
    def create_component_palette(self):
        """Crée la palette de composants"""
        components = [
            ("Résistance", "resistor"),
            ("Pile", "battery"),
            ("LED", "led"),
            ("Interrupteur", "switch"),
        ]
        
        for name, comp_type in components:
            btn = ttk.Button(self.palette_frame, text=name, 
                           command=lambda t=comp_type: self.add_component(t))
            btn.pack(fill='x', pady=2)
            
        # Séparateur
        ttk.Separator(self.palette_frame, orient='horizontal').pack(
            fill='x', pady=10)
            
        # Instructions
        instructions = tk.Text(self.palette_frame, height=12, width=20, 
                              wrap='word', relief='flat', bg='#F0F0F0')
        instructions.pack(fill='both', expand=True)
        instructions.insert('1.0', 
            "Instructions:\n\n"
            "1. Cliquez sur un composant pour l'ajouter\n\n"
            "2. Connecter les fils:\n"
            "   - Clic sur un composant\n"
            "   - Clic sur un autre composant\n\n"
            "3. Supprimer:\n"
            "   - Clic droit sur un élément\n\n"
            "4. Thèmes:\n"
            "   - Menu Apparence"
        )
        instructions.config(state='disabled')
        
    def configure_grid_weights(self):
        """Configure les poids pour le redimensionnement"""
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Main frame weights
        main_frame = self.root.winfo_children()[0]
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=0)  # Palette fixe
        main_frame.grid_columnconfigure(1, weight=1)  # Canvas extensible
        main_frame.grid_columnconfigure(2, weight=0)  # Propriétés fixe
        
    def add_component(self, comp_type):
        """Ajoute un composant au centre du canvas"""
        # Position par défaut au centre
        x = 400
        y = 300
        
        component = self.circuit_manager.add_component(comp_type, x, y)
        if component:
            self.canvas.redraw()
            
    def calculate_circuit(self):
        """Calcule les valeurs du circuit"""
        results = self.circuit_manager.calculate_circuit()
        
        # Afficher les résultats
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', 'end')
        
        text = "Résultats du circuit:\n\n"
        text += f"Tension totale: {results['voltage']:.2f} V\n"
        text += f"Résistance totale: {results['total_resistance']:.2f} Ω\n"
        text += f"Courant: {results['current']*1000:.2f} mA\n"
        
        self.results_text.insert('1.0', text)
        self.results_text.config(state='disabled')
        
    def new_circuit(self):
        """Crée un nouveau circuit"""
        if messagebox.askyesno("Nouveau circuit", 
                              "Effacer le circuit actuel ?"):
            self.clear_circuit()
            
    def clear_circuit(self):
        """Efface le circuit"""
        self.circuit_manager.clear()
        self.canvas.redraw()
        
        # Effacer les résultats
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', 'end')
        self.results_text.config(state='disabled')
        
    def apply_theme_by_id(self, theme_id):
        """Applique un thème par son ID"""
        self.theme_manager.apply_theme(theme_id)
        self.apply_theme()
        
    def apply_theme(self):
        """Applique le thème actuel à toute l'interface"""
        theme = self.theme_manager.get_current_theme()
        
        # Style ttk
        style = ttk.Style()
        style.configure('TFrame', background=theme['ui_bg'])
        style.configure('TLabelframe', background=theme['ui_bg'])
        style.configure('TLabelframe.Label', background=theme['ui_bg'], 
                       foreground=theme['text_color'])
        style.configure('TLabel', background=theme['ui_bg'], 
                       foreground=theme['text_color'])
        style.configure('TButton', background=theme['button_bg'])
        
        # Appliquer au canvas
        self.canvas.apply_theme()
        
        # Appliquer aux frames
        self.root.configure(bg=theme['ui_bg'])
        
    def load_background_image(self):
        """Charge une image de fond via dialogue"""
        from tkinter import filedialog
        filename = filedialog.askopenfilename(
            title="Choisir une image de fond",
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("Tous les fichiers", "*.*")
            ]
        )
        if filename:
            self.theme_manager.load_background_image(filename)
            self.canvas.redraw()
            
    def remove_background_image(self):
        """Supprime l'image de fond"""
        self.theme_manager.remove_background_image()
        self.canvas.redraw()
        
    def open_theme_dialog(self):
        """Ouvre le dialogue de personnalisation"""
        ThemeDialog(self.root, self.theme_manager, self.apply_theme)
        
    def show_about(self):
        """Affiche la boîte de dialogue À propos"""
        messagebox.showinfo("À propos", 
            "Concepteur de Circuits Électroniques\n\n"
            "Version 1.0\n\n"
            "Fonctionnalités:\n"
            "- Dessin de circuits\n"
            "- Connexion de fils\n"
            "- Calculs électriques\n"
            "- Thèmes personnalisables\n"
            "- Images de fond"
        )
