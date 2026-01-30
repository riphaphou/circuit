# -*- coding: utf-8 -*-
"""
Canvas de dessin du circuit avec gestion de la grille et de l'image de fond
"""

import tkinter as tk
from PIL import Image, ImageTk

class CircuitCanvas(tk.Canvas):
    """Canvas personnalisé pour dessiner des circuits"""
    
    def __init__(self, parent, circuit_manager, theme_manager, **kwargs):
        super().__init__(parent, **kwargs)
        self.circuit_manager = circuit_manager
        self.theme_manager = theme_manager
        self.grid_size = 20
        
        # Gestion de l'image de fond
        self.background_image = None
        self.background_photo = None
        
        # Gestion du fil en cours de création
        self.wire_start_component = None
        self.wire_start_pin = None
        self.temp_wire_line = None
        
        # Composant sélectionné pour déplacement
        self.selected_component = None
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Binding des événements
        self.bind('<Button-1>', self.on_canvas_click)
        self.bind('<B1-Motion>', self.on_canvas_drag)
        self.bind('<ButtonRelease-1>', self.on_canvas_release)
        self.bind('<Motion>', self.on_canvas_motion)
        self.bind('<Button-3>', self.on_right_click)
        
        # Appliquer le thème initial
        self.apply_theme()
        
    def apply_theme(self):
        """Applique le thème actuel au canvas"""
        theme = self.theme_manager.get_current_theme()
        self.configure(bg=theme['canvas_bg'])
        self.redraw()
        
    def load_background_image(self):
        """Charge et affiche l'image de fond"""
        if not self.theme_manager.background_image_path:
            self.background_image = None
            self.background_photo = None
            return
            
        try:
            # Charger l'image
            img = Image.open(self.theme_manager.background_image_path)
            
            # Obtenir les dimensions du canvas
            canvas_width = self.winfo_width()
            canvas_height = self.winfo_height()
            
            if canvas_width <= 1:
                canvas_width = 800
            if canvas_height <= 1:
                canvas_height = 600
            
            # Appliquer le mode d'affichage
            if self.theme_manager.background_mode == 'stretch':
                img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            elif self.theme_manager.background_mode == 'center':
                # Créer une nouvelle image de la taille du canvas
                new_img = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))
                # Centrer l'image originale
                x = (canvas_width - img.width) // 2
                y = (canvas_height - img.height) // 2
                new_img.paste(img, (x, y))
                img = new_img
            elif self.theme_manager.background_mode == 'tile':
                # Créer une image en mosaïque
                new_img = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))
                for x in range(0, canvas_width, img.width):
                    for y in range(0, canvas_height, img.height):
                        new_img.paste(img, (x, y))
                img = new_img
            
            # Appliquer l'opacité
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            alpha = int(255 * (self.theme_manager.background_opacity / 100))
            img.putalpha(alpha)
            
            # Convertir pour Tkinter
            self.background_photo = ImageTk.PhotoImage(img)
            self.background_image = img
            
        except Exception as e:
            print(f"Erreur lors du chargement de l'image de fond: {e}")
            self.background_image = None
            self.background_photo = None
            
    def draw_grid(self):
        """Dessine la grille sur le canvas"""
        theme = self.theme_manager.get_current_theme()
        grid_color = theme['grid_color']
        
        width = self.winfo_width()
        height = self.winfo_height()
        
        # Lignes verticales
        for x in range(0, width, self.grid_size):
            self.create_line(x, 0, x, height, fill=grid_color, tags='grid')
            
        # Lignes horizontales
        for y in range(0, height, self.grid_size):
            self.create_line(0, y, width, y, fill=grid_color, tags='grid')
            
    def redraw(self):
        """Redessine tout le canvas"""
        self.delete('all')
        
        # Dessiner l'image de fond si présente
        if self.theme_manager.background_image_path:
            self.load_background_image()
            if self.background_photo:
                self.create_image(0, 0, image=self.background_photo, 
                                 anchor='nw', tags='background')
        
        # Dessiner la grille
        self.draw_grid()
        
        # Dessiner les fils
        theme = self.theme_manager.get_current_theme()
        for wire in self.circuit_manager.wires.values():
            wire.draw(self, theme)
            
        # Dessiner les composants
        for component in self.circuit_manager.components.values():
            component.draw(self, theme)
            
    def on_canvas_click(self, event):
        """Gestion du clic gauche"""
        x, y = event.x, event.y
        
        # Vérifier si on clique sur un composant
        component = self.circuit_manager.get_component_at(x, y)
        
        if component:
            # Si on commence un fil
            if self.wire_start_component is None:
                # Démarrer un fil
                pin = component.get_nearest_pin(x, y)
                if pin:
                    self.wire_start_component = component
                    self.wire_start_pin = pin
                    # Dessiner une ligne temporaire
                    theme = self.theme_manager.get_current_theme()
                    self.temp_wire_line = self.create_line(
                        pin[0], pin[1], x, y,
                        fill=theme.get('wire_color', '#FF0000'),
                        width=2, dash=(5, 5), tags='temp_wire'
                    )
            else:
                # Terminer un fil
                pin = component.get_nearest_pin(x, y)
                if pin and component != self.wire_start_component:
                    # Créer le fil
                    wire = self.circuit_manager.add_wire(
                        self.wire_start_component.id, self.wire_start_pin,
                        component.id, pin
                    )
                    if wire:
                        theme = self.theme_manager.get_current_theme()
                        wire.draw(self, theme)
                        
                # Réinitialiser
                self.wire_start_component = None
                self.wire_start_pin = None
                if self.temp_wire_line:
                    self.delete(self.temp_wire_line)
                    self.temp_wire_line = None
                    
    def on_canvas_drag(self, event):
        """Gestion du glissement (drag)"""
        if self.temp_wire_line:
            # Mettre à jour la ligne temporaire
            coords = self.coords(self.temp_wire_line)
            if len(coords) >= 4:
                self.coords(self.temp_wire_line, 
                           coords[0], coords[1], event.x, event.y)
                           
    def on_canvas_release(self, event):
        """Gestion du relâchement du bouton"""
        pass
        
    def on_canvas_motion(self, event):
        """Gestion du mouvement de la souris"""
        # Afficher un feedback visuel si on survole une borne
        if self.wire_start_component:
            x, y = event.x, event.y
            component = self.circuit_manager.get_component_at(x, y)
            if component and component != self.wire_start_component:
                pin = component.get_nearest_pin(x, y)
                if pin:
                    # Accrocher à la borne
                    if self.temp_wire_line:
                        coords = self.coords(self.temp_wire_line)
                        if len(coords) >= 4:
                            self.coords(self.temp_wire_line,
                                       coords[0], coords[1], pin[0], pin[1])
                                       
    def on_right_click(self, event):
        """Gestion du clic droit (menu contextuel)"""
        x, y = event.x, event.y
        
        # Vérifier si on clique sur un fil
        items = self.find_overlapping(x-5, y-5, x+5, y+5)
        for item in items:
            tags = self.gettags(item)
            for tag in tags:
                if tag.startswith('wire_'):
                    wire_id = int(tag.split('_')[1])
                    # Supprimer le fil
                    self.circuit_manager.remove_wire(wire_id)
                    self.redraw()
                    return
                    
        # Vérifier si on clique sur un composant
        component = self.circuit_manager.get_component_at(x, y)
        if component:
            # Créer un menu contextuel
            menu = tk.Menu(self, tearoff=0)
            menu.add_command(label="Supprimer", 
                           command=lambda: self.delete_component(component.id))
            menu.post(event.x_root, event.y_root)
            
    def delete_component(self, comp_id):
        """Supprime un composant"""
        self.circuit_manager.remove_component(comp_id)
        self.redraw()
        
    def snap_to_grid(self, x, y):
        """Accroche les coordonnées à la grille"""
        return (round(x / self.grid_size) * self.grid_size,
                round(y / self.grid_size) * self.grid_size)
