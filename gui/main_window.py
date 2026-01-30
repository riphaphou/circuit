"""
Fenêtre principale de l'application.
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from gui.canvas import CircuitCanvas
from gui.component_palette import ComponentPalette
from gui.properties_panel import PropertiesPanel
from circuit import CircuitManager, CircuitCalculator, CircuitAnalyzer
from utils import FileManager


class MainWindow(tk.Tk):
    """Fenêtre principale de l'application Circuit Designer."""
    
    def __init__(self):
        """Initialise la fenêtre principale."""
        super().__init__()
        
        self.title("Circuit Designer - Outil de conception de circuits électroniques")
        self.geometry("1200x800")
        
        # Gestionnaire de circuit
        self.circuit_manager = CircuitManager()
        self.calculator = CircuitCalculator(self.circuit_manager)
        self.analyzer = CircuitAnalyzer(self.circuit_manager)
        
        # Créer l'interface
        self.create_menu()
        self.create_toolbar()
        self.create_main_layout()
        self.create_results_panel()
        
        # Fichier actuel
        self.current_file = None
    
    def create_menu(self):
        """Crée la barre de menu."""
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # Menu Fichier
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Nouveau", command=self.new_circuit, accelerator="Ctrl+N")
        file_menu.add_command(label="Ouvrir...", command=self.open_circuit, accelerator="Ctrl+O")
        file_menu.add_command(label="Sauvegarder", command=self.save_circuit, accelerator="Ctrl+S")
        file_menu.add_command(label="Sauvegarder sous...", command=self.save_circuit_as)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit_app, accelerator="Ctrl+Q")
        
        # Menu Édition
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Édition", menu=edit_menu)
        edit_menu.add_command(label="Effacer tout", command=self.clear_circuit)
        
        # Menu Circuit
        circuit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Circuit", menu=circuit_menu)
        circuit_menu.add_command(label="Calculer", command=self.calculate_circuit, accelerator="F5")
        circuit_menu.add_command(label="Analyser", command=self.analyze_circuit)
        
        # Menu Aide
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="À propos", command=self.show_about)
        help_menu.add_command(label="Guide d'utilisation", command=self.show_help)
        
        # Raccourcis clavier
        self.bind("<Control-n>", lambda e: self.new_circuit())
        self.bind("<Control-o>", lambda e: self.open_circuit())
        self.bind("<Control-s>", lambda e: self.save_circuit())
        self.bind("<Control-q>", lambda e: self.quit_app())
        self.bind("<F5>", lambda e: self.calculate_circuit())
    
    def create_toolbar(self):
        """Crée la barre d'outils."""
        toolbar = ttk.Frame(self, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)
        
        # Boutons
        ttk.Button(toolbar, text="📄 Nouveau", command=self.new_circuit).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📁 Ouvrir", command=self.open_circuit).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="💾 Sauvegarder", command=self.save_circuit).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        ttk.Button(toolbar, text="🧹 Effacer", command=self.clear_circuit).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🔬 Calculer", command=self.calculate_circuit).pack(side=tk.LEFT, padx=2)
        
        # Info à droite
        info_label = ttk.Label(toolbar, text="Circuit Designer v1.0", font=("Arial", 9))
        info_label.pack(side=tk.RIGHT, padx=10)
    
    def create_main_layout(self):
        """Crée la disposition principale."""
        # Frame principal
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Panneau gauche - Palette de composants
        left_panel = ttk.LabelFrame(main_frame, text="Palette", width=150)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        left_panel.pack_propagate(False)
        
        # Canvas central
        center_panel = ttk.LabelFrame(main_frame, text="Circuit")
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Canvas de dessin
        self.canvas = CircuitCanvas(
            center_panel, 
            self.circuit_manager,
            bg="white",
            width=700,
            height=500
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Panneau droit - Propriétés
        right_panel = ttk.LabelFrame(main_frame, text="Propriétés", width=200)
        right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
        right_panel.pack_propagate(False)
        
        # Créer les sous-panneaux
        self.palette = ComponentPalette(left_panel, self.canvas)
        self.palette.pack(fill=tk.BOTH, expand=True)
        
        self.properties = PropertiesPanel(right_panel, self.canvas)
        self.properties.pack(fill=tk.BOTH, expand=True)
    
    def create_results_panel(self):
        """Crée le panneau de résultats."""
        results_frame = ttk.LabelFrame(self, text="Résultats des calculs")
        results_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        # Zone de texte pour les résultats
        self.results_text = tk.Text(results_frame, height=8, wrap=tk.WORD, bg="#f0f0f0")
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.results_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.results_text.yview)
    
    def new_circuit(self):
        """Crée un nouveau circuit."""
        if messagebox.askyesno("Nouveau circuit", 
                              "Créer un nouveau circuit? Les modifications non sauvegardées seront perdues."):
            self.circuit_manager.clear()
            self.canvas.clear_canvas()
            self.current_file = None
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, "Nouveau circuit créé.\n")
    
    def open_circuit(self):
        """Ouvre un circuit depuis un fichier."""
        filepath = filedialog.askopenfilename(
            title="Ouvrir un circuit",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )
        
        if filepath:
            if FileManager.load_circuit(self.circuit_manager, filepath):
                self.current_file = filepath
                self.canvas.redraw_all()
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(1.0, f"Circuit chargé depuis: {filepath}\n")
                messagebox.showinfo("Succès", "Circuit chargé avec succès")
            else:
                messagebox.showerror("Erreur", "Impossible de charger le circuit")
    
    def save_circuit(self):
        """Sauvegarde le circuit."""
        if self.current_file:
            if FileManager.save_circuit(self.circuit_manager, self.current_file):
                self.results_text.insert(tk.END, f"Circuit sauvegardé: {self.current_file}\n")
                messagebox.showinfo("Succès", "Circuit sauvegardé")
            else:
                messagebox.showerror("Erreur", "Impossible de sauvegarder le circuit")
        else:
            self.save_circuit_as()
    
    def save_circuit_as(self):
        """Sauvegarde le circuit sous un nouveau nom."""
        filepath = filedialog.asksaveasfilename(
            title="Sauvegarder le circuit",
            defaultextension=".json",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )
        
        if filepath:
            if FileManager.save_circuit(self.circuit_manager, filepath):
                self.current_file = filepath
                self.results_text.insert(tk.END, f"Circuit sauvegardé: {filepath}\n")
                messagebox.showinfo("Succès", "Circuit sauvegardé")
            else:
                messagebox.showerror("Erreur", "Impossible de sauvegarder le circuit")
    
    def clear_circuit(self):
        """Efface tout le circuit."""
        if messagebox.askyesno("Confirmation", 
                              "Effacer tout le circuit?"):
            self.circuit_manager.clear()
            self.canvas.clear_canvas()
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, "Circuit effacé.\n")
    
    def calculate_circuit(self):
        """Calcule les grandeurs électriques du circuit."""
        # Vérifier si le circuit est valide
        valid, message = self.analyzer.is_circuit_valid()
        
        if not valid:
            messagebox.showwarning("Circuit invalide", message)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, f"Erreur: {message}\n")
            return
        
        # Effectuer les calculs
        results = self.calculator.analyze_circuit()
        
        # Afficher les résultats
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, self.calculator.format_results())
        
        messagebox.showinfo("Calculs terminés", "Les calculs ont été effectués avec succès")
    
    def analyze_circuit(self):
        """Analyse la topologie du circuit."""
        info = self.analyzer.get_circuit_info()
        
        message = f"""Informations du circuit:
        
Nombre de composants: {info['num_components']}
Nombre de fils: {info['num_wires']}
Nombre de résistances: {info['num_resistors']}
Sources de tension: {info['num_voltage_sources']}
Sources de courant: {info['num_current_sources']}
Type de circuit: {info['circuit_type']}
Validité: {info['valid'][1]}
"""
        
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, message)
    
    def show_about(self):
        """Affiche la boîte À propos."""
        about_text = """Circuit Designer v1.0

Outil de conception et d'analyse de circuits électroniques

Développé avec Python et Tkinter

Fonctionnalités:
- Éditeur graphique de schémas
- Calculs électriques automatiques
- Sauvegarde/Chargement JSON
- Support de multiples composants

© 2024"""
        messagebox.showinfo("À propos", about_text)
    
    def show_help(self):
        """Affiche l'aide."""
        help_text = """Guide d'utilisation:

1. Ajout de composants:
   - Cliquez sur un composant dans la palette
   - Cliquez sur le canvas pour le placer

2. Modification:
   - Cliquez droit sur un composant
   - Modifiez les propriétés dans le panneau
   - Cliquez sur 'Appliquer'

3. Déplacement:
   - Glissez-déposez les composants

4. Calculs:
   - Ajoutez des composants et sources
   - Cliquez sur 'Calculer' (F5)
   - Les résultats s'affichent en bas

5. Sauvegarde:
   - Menu Fichier > Sauvegarder
   - Format JSON"""
        messagebox.showinfo("Aide", help_text)
    
    def quit_app(self):
        """Quitte l'application."""
        if messagebox.askyesno("Quitter", 
                              "Voulez-vous vraiment quitter?"):
            self.destroy()
