# -*- coding: utf-8 -*-
"""
Fenêtre de dialogue pour la personnalisation des thèmes
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class ThemeDialog(tk.Toplevel):
    """Dialogue de personnalisation des thèmes"""
    
    def __init__(self, parent, theme_manager, on_apply_callback):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.on_apply_callback = on_apply_callback
        
        self.title("Personnalisation de l'apparence")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Centrer la fenêtre
        self.transient(parent)
        self.grab_set()
        
        self.create_widgets()
        
    def create_widgets(self):
        """Crée les widgets du dialogue"""
        # Frame principal
        main_frame = ttk.Frame(self, padding=10)
        main_frame.pack(fill='both', expand=True)
        
        # Section Thèmes
        theme_label = ttk.Label(main_frame, text="Thème:", font=('Arial', 12, 'bold'))
        theme_label.pack(anchor='w', pady=(0, 5))
        
        # Liste des thèmes
        self.theme_var = tk.StringVar(value=self.theme_manager.current_theme)
        theme_frame = ttk.Frame(main_frame)
        theme_frame.pack(fill='x', pady=(0, 15))
        
        for theme_id, theme_name in self.theme_manager.get_theme_names():
            rb = ttk.Radiobutton(theme_frame, text=theme_name, 
                                variable=self.theme_var, value=theme_id,
                                command=self.apply_theme_preview)
            rb.pack(anchor='w', padx=20)
            
        # Séparateur
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)
        
        # Section Image de fond
        bg_label = ttk.Label(main_frame, text="Image de fond:", 
                            font=('Arial', 12, 'bold'))
        bg_label.pack(anchor='w', pady=(0, 5))
        
        # Boutons image de fond
        bg_buttons_frame = ttk.Frame(main_frame)
        bg_buttons_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Button(bg_buttons_frame, text="Charger image...", 
                  command=self.load_background).pack(side='left', padx=5)
        ttk.Button(bg_buttons_frame, text="Supprimer image", 
                  command=self.remove_background).pack(side='left', padx=5)
        
        # Label du fichier actuel
        self.bg_file_label = ttk.Label(main_frame, text="Aucune image", 
                                      foreground='gray')
        self.bg_file_label.pack(anchor='w', padx=20)
        self.update_bg_label()
        
        # Opacité
        opacity_frame = ttk.Frame(main_frame)
        opacity_frame.pack(fill='x', pady=10, padx=20)
        
        ttk.Label(opacity_frame, text="Opacité:").pack(side='left')
        self.opacity_var = tk.IntVar(value=self.theme_manager.background_opacity)
        opacity_scale = ttk.Scale(opacity_frame, from_=0, to=100, 
                                 variable=self.opacity_var, orient='horizontal',
                                 command=self.on_opacity_change)
        opacity_scale.pack(side='left', fill='x', expand=True, padx=10)
        self.opacity_label = ttk.Label(opacity_frame, text="100%", width=5)
        self.opacity_label.pack(side='left')
        
        # Mode d'affichage
        mode_frame = ttk.Frame(main_frame)
        mode_frame.pack(fill='x', pady=10, padx=20)
        
        ttk.Label(mode_frame, text="Mode:").pack(side='left')
        self.mode_var = tk.StringVar(value=self.theme_manager.background_mode)
        mode_combo = ttk.Combobox(mode_frame, textvariable=self.mode_var,
                                 values=['stretch', 'tile', 'center'],
                                 state='readonly', width=15)
        mode_combo.pack(side='left', padx=10)
        mode_combo.bind('<<ComboboxSelected>>', self.on_mode_change)
        
        # Boutons de fermeture
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side='bottom', fill='x', pady=(20, 0))
        
        ttk.Button(button_frame, text="Appliquer et fermer", 
                  command=self.apply_and_close).pack(side='right', padx=5)
        ttk.Button(button_frame, text="Annuler", 
                  command=self.destroy).pack(side='right', padx=5)
                  
    def apply_theme_preview(self):
        """Applique un aperçu du thème sélectionné"""
        theme_id = self.theme_var.get()
        self.theme_manager.apply_theme(theme_id)
        self.on_apply_callback()
        
    def load_background(self):
        """Charge une image de fond"""
        filename = filedialog.askopenfilename(
            title="Choisir une image de fond",
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("PNG", "*.png"),
                ("JPEG", "*.jpg *.jpeg"),
                ("GIF", "*.gif"),
                ("Tous les fichiers", "*.*")
            ]
        )
        if filename:
            if self.theme_manager.load_background_image(filename):
                self.update_bg_label()
                self.on_apply_callback()
            else:
                messagebox.showerror("Erreur", 
                                   "Impossible de charger l'image")
                                   
    def remove_background(self):
        """Supprime l'image de fond"""
        self.theme_manager.remove_background_image()
        self.update_bg_label()
        self.on_apply_callback()
        
    def update_bg_label(self):
        """Met à jour le label du fichier d'image"""
        if self.theme_manager.background_image_path:
            import os
            filename = os.path.basename(self.theme_manager.background_image_path)
            self.bg_file_label.config(text=f"Image: {filename}", 
                                     foreground='black')
        else:
            self.bg_file_label.config(text="Aucune image", 
                                     foreground='gray')
                                     
    def on_opacity_change(self, value):
        """Gestion du changement d'opacité"""
        opacity = int(float(value))
        self.opacity_label.config(text=f"{opacity}%")
        self.theme_manager.set_background_opacity(opacity)
        self.on_apply_callback()
        
    def on_mode_change(self, event):
        """Gestion du changement de mode"""
        mode = self.mode_var.get()
        self.theme_manager.set_background_mode(mode)
        self.on_apply_callback()
        
    def apply_and_close(self):
        """Applique les changements et ferme la fenêtre"""
        self.destroy()
