# -*- coding: utf-8 -*-
"""
Gestionnaire de thèmes et de préférences
"""

import json
import os
from pathlib import Path

class ThemeManager:
    """Gestionnaire des thèmes et de la personnalisation"""
    
    # Définition des thèmes prédéfinis
    THEMES = {
        'light': {
            'name': 'Clair',
            'canvas_bg': '#FFFFFF',
            'grid_color': '#E0E0E0',
            'component_color': '#000000',
            'text_color': '#000000',
            'wire_color': '#FF0000',
            'ui_bg': '#F5F5F5',
            'panel_bg': '#FFFFFF',
            'button_bg': '#E0E0E0',
        },
        'dark': {
            'name': 'Sombre',
            'canvas_bg': '#2B2B2B',
            'grid_color': '#404040',
            'component_color': '#FFFFFF',
            'text_color': '#FFFFFF',
            'wire_color': '#FF6B6B',
            'ui_bg': '#1E1E1E',
            'panel_bg': '#252525',
            'button_bg': '#3C3C3C',
        },
        'blue': {
            'name': 'Bleu',
            'canvas_bg': '#E3F2FD',
            'grid_color': '#BBDEFB',
            'component_color': '#1976D2',
            'text_color': '#0D47A1',
            'wire_color': '#1976D2',
            'ui_bg': '#F5F9FF',
            'panel_bg': '#E3F2FD',
            'button_bg': '#BBDEFB',
        },
        'green': {
            'name': 'Vert (confort)',
            'canvas_bg': '#E8F5E9',
            'grid_color': '#C8E6C9',
            'component_color': '#388E3C',
            'text_color': '#1B5E20',
            'wire_color': '#388E3C',
            'ui_bg': '#F1F8E9',
            'panel_bg': '#E8F5E9',
            'button_bg': '#C8E6C9',
        },
    }
    
    def __init__(self):
        self.current_theme = 'light'
        self.background_image_path = None
        self.background_opacity = 100
        self.background_mode = 'stretch'  # stretch, tile, center
        self.preferences_file = Path.home() / '.circuit_preferences.json'
        self.load_preferences()
        
    def get_current_theme(self):
        """Retourne le thème actuel"""
        return self.THEMES.get(self.current_theme, self.THEMES['light'])
        
    def apply_theme(self, theme_name):
        """Applique un thème prédéfini"""
        if theme_name in self.THEMES:
            self.current_theme = theme_name
            self.save_preferences()
            return True
        return False
        
    def get_theme_names(self):
        """Retourne la liste des noms de thèmes disponibles"""
        return [(key, value['name']) for key, value in self.THEMES.items()]
        
    def load_background_image(self, path):
        """Charge une image de fond"""
        if os.path.exists(path):
            self.background_image_path = path
            self.save_preferences()
            return True
        return False
        
    def remove_background_image(self):
        """Supprime l'image de fond"""
        self.background_image_path = None
        self.save_preferences()
        
    def set_background_opacity(self, opacity):
        """Définit l'opacité de l'image de fond (0-100)"""
        self.background_opacity = max(0, min(100, opacity))
        self.save_preferences()
        
    def set_background_mode(self, mode):
        """Définit le mode d'affichage de l'image de fond"""
        if mode in ['stretch', 'tile', 'center']:
            self.background_mode = mode
            self.save_preferences()
            
    def save_preferences(self):
        """Sauvegarde les préférences dans un fichier JSON"""
        preferences = {
            'theme': self.current_theme,
            'background_image': self.background_image_path,
            'background_opacity': self.background_opacity,
            'background_mode': self.background_mode,
        }
        try:
            with open(self.preferences_file, 'w', encoding='utf-8') as f:
                json.dump(preferences, f, indent=2)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des préférences: {e}")
            
    def load_preferences(self):
        """Charge les préférences depuis le fichier JSON"""
        if self.preferences_file.exists():
            try:
                with open(self.preferences_file, 'r', encoding='utf-8') as f:
                    preferences = json.load(f)
                    self.current_theme = preferences.get('theme', 'light')
                    self.background_image_path = preferences.get('background_image')
                    self.background_opacity = preferences.get('background_opacity', 100)
                    self.background_mode = preferences.get('background_mode', 'stretch')
            except Exception as e:
                print(f"Erreur lors du chargement des préférences: {e}")
