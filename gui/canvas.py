"""
Canvas de dessin pour les circuits électroniques.
"""
import tkinter as tk
from components import Resistor, VoltageSource, CurrentSource, Capacitor, Inductor, Wire


class CircuitCanvas(tk.Canvas):
    """Canvas pour dessiner et manipuler les composants du circuit."""
    
    # Constantes
    COMPONENT_CLICK_TOLERANCE = 50  # Distance max en pixels pour cliquer sur un composant
    
    def __init__(self, master, circuit_manager, **kwargs):
        """
        Initialise le canvas.
        
        Args:
            master: Widget parent
            circuit_manager: Gestionnaire de circuit
            **kwargs: Arguments pour tk.Canvas
        """
        super().__init__(master, **kwargs)
        self.circuit_manager = circuit_manager
        self.selected_component = None
        self.drag_data = {"x": 0, "y": 0, "item": None}
        self.drawing_wire = False
        self.wire_start = None
        self.temp_wire_id = None
        self.snap_to_grid = True
        self.grid_size = 20
        self.component_to_place = None  # Type de composant à placer
        
        # Bindings pour la manipulation
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)
        self.bind("<Button-3>", self.on_right_click)
        
        # Redessiner la grille lors du redimensionnement
        self.bind("<Configure>", self.on_resize)
        
        # Dessiner la grille initiale
        self.draw_grid()
    
    def draw_grid(self):
        """Dessine une grille sur le canvas."""
        # Supprimer l'ancienne grille
        self.delete("grid")
        
        # Obtenir les dimensions actuelles du canvas
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        
        # Utiliser des dimensions minimales si le canvas n'est pas encore affiché
        if width <= 1:
            width = 700
        if height <= 1:
            height = 500
        
        # Lignes verticales
        for x in range(0, width, self.grid_size):
            self.create_line(x, 0, x, height, fill="#e0e0e0", tags="grid")
        
        # Lignes horizontales
        for y in range(0, height, self.grid_size):
            self.create_line(0, y, width, y, fill="#e0e0e0", tags="grid")
        
        # Mettre la grille en arrière-plan
        self.tag_lower("grid")
    
    def on_resize(self, event):
        """Gestionnaire de redimensionnement du canvas."""
        # Redessiner la grille avec les nouvelles dimensions
        self.draw_grid()
    
    def snap_position(self, x, y):
        """
        Aligne une position sur la grille.
        
        Args:
            x, y: Coordonnées
            
        Returns:
            tuple: Coordonnées alignées
        """
        if self.snap_to_grid:
            x = round(x / self.grid_size) * self.grid_size
            y = round(y / self.grid_size) * self.grid_size
        return x, y
    
    def set_component_to_place(self, component_type):
        """
        Définit le type de composant à placer au prochain clic.
        
        Args:
            component_type: Classe du composant à placer
        """
        self.component_to_place = component_type
        self.drawing_wire = False  # Désactiver le mode fil
        self.config(cursor="crosshair")
    
    def start_wire_mode(self):
        """
        Active le mode de création de fil.
        L'utilisateur doit cliquer sur deux composants pour créer un fil.
        """
        self.drawing_wire = True
        self.wire_start = None
        self.component_to_place = None  # Désactiver le mode placement
        self.config(cursor="plus")
    
    def add_component(self, component_type, x, y):
        """
        Ajoute un composant au circuit.
        
        Args:
            component_type: Type de composant à créer
            x, y: Position
            
        Returns:
            Composant créé
        """
        x, y = self.snap_position(x, y)
        
        # Créer le composant approprié
        component = component_type(x=x, y=y)
        self.circuit_manager.add_component(component)
        
        # Dessiner le composant
        self.draw_component(component)
        
        return component
    
    def draw_component(self, component):
        """
        Dessine un composant sur le canvas.
        
        Args:
            component: Composant à dessiner
        """
        x, y = component.x, component.y
        
        # Effacer l'ancien dessin si présent
        if component.canvas_id:
            self.delete(component.canvas_id)
        
        # Dessiner selon le type
        if isinstance(component, Resistor):
            component.canvas_id = self.draw_resistor(x, y, component.name, component.value)
        elif isinstance(component, VoltageSource):
            component.canvas_id = self.draw_voltage_source(x, y, component.name, component.value)
        elif isinstance(component, CurrentSource):
            component.canvas_id = self.draw_current_source(x, y, component.name, component.value)
        elif isinstance(component, Capacitor):
            component.canvas_id = self.draw_capacitor(x, y, component.name, component.value)
        elif isinstance(component, Inductor):
            component.canvas_id = self.draw_inductor(x, y, component.name, component.value)
        elif isinstance(component, Wire):
            component.canvas_id = self.draw_wire(component)
    
    def draw_resistor(self, x, y, name, value):
        """Dessine une résistance."""
        # Rectangle en zigzag
        tag = f"comp_{name}"
        self.create_rectangle(x-30, y-10, x+30, y+10, fill="white", outline="black", width=2, tags=tag)
        self.create_text(x, y-20, text=name, tags=tag, font=("Arial", 10, "bold"))
        self.create_text(x, y+20, text=f"{value}Ω", tags=tag, font=("Arial", 9))
        
        # Terminaux
        self.create_line(x-40, y, x-30, y, width=2, tags=tag)
        self.create_line(x+30, y, x+40, y, width=2, tags=tag)
        self.create_oval(x-42, y-2, x-38, y+2, fill="red", outline="red", tags=tag)
        self.create_oval(x+38, y-2, x+42, y+2, fill="red", outline="red", tags=tag)
        
        return tag
    
    def draw_voltage_source(self, x, y, name, value):
        """Dessine une source de tension."""
        tag = f"comp_{name}"
        # Cercle
        self.create_oval(x-25, y-25, x+25, y+25, fill="white", outline="black", width=2, tags=tag)
        self.create_text(x, y, text=f"{value}V", tags=tag, font=("Arial", 10, "bold"))
        self.create_text(x, y-35, text=name, tags=tag, font=("Arial", 10, "bold"))
        
        # Polarité
        self.create_text(x-15, y, text="+", tags=tag, font=("Arial", 12, "bold"), fill="red")
        self.create_text(x+15, y, text="-", tags=tag, font=("Arial", 12, "bold"), fill="blue")
        
        # Terminaux
        self.create_line(x-40, y, x-25, y, width=2, tags=tag)
        self.create_line(x+25, y, x+40, y, width=2, tags=tag)
        self.create_oval(x-42, y-2, x-38, y+2, fill="red", outline="red", tags=tag)
        self.create_oval(x+38, y-2, x+42, y+2, fill="red", outline="red", tags=tag)
        
        return tag
    
    def draw_current_source(self, x, y, name, value):
        """Dessine une source de courant."""
        tag = f"comp_{name}"
        # Cercle
        self.create_oval(x-25, y-25, x+25, y+25, fill="white", outline="black", width=2, tags=tag)
        # Flèche
        self.create_line(x-15, y, x+15, y, width=2, arrow=tk.LAST, tags=tag)
        self.create_text(x, y-35, text=name, tags=tag, font=("Arial", 10, "bold"))
        self.create_text(x, y+35, text=f"{value*1000:.1f}mA", tags=tag, font=("Arial", 9))
        
        # Terminaux
        self.create_line(x-40, y, x-25, y, width=2, tags=tag)
        self.create_line(x+25, y, x+40, y, width=2, tags=tag)
        self.create_oval(x-42, y-2, x-38, y+2, fill="red", outline="red", tags=tag)
        self.create_oval(x+38, y-2, x+42, y+2, fill="red", outline="red", tags=tag)
        
        return tag
    
    def draw_capacitor(self, x, y, name, value):
        """Dessine un condensateur."""
        tag = f"comp_{name}"
        # Deux lignes parallèles
        self.create_line(x-5, y-20, x-5, y+20, width=3, tags=tag)
        self.create_line(x+5, y-20, x+5, y+20, width=3, tags=tag)
        self.create_text(x, y-30, text=name, tags=tag, font=("Arial", 10, "bold"))
        self.create_text(x, y+30, text=f"{value*1000000:.1f}µF", tags=tag, font=("Arial", 9))
        
        # Terminaux
        self.create_line(x-40, y, x-5, y, width=2, tags=tag)
        self.create_line(x+5, y, x+40, y, width=2, tags=tag)
        self.create_oval(x-42, y-2, x-38, y+2, fill="red", outline="red", tags=tag)
        self.create_oval(x+38, y-2, x+42, y+2, fill="red", outline="red", tags=tag)
        
        return tag
    
    def draw_inductor(self, x, y, name, value):
        """Dessine une inductance."""
        tag = f"comp_{name}"
        # Spirales (simplifiées avec des arcs)
        for i in range(4):
            arc_x = x - 20 + i * 10
            self.create_arc(arc_x, y-10, arc_x+10, y+10, start=180, extent=180, 
                          style=tk.ARC, width=2, tags=tag)
        
        self.create_text(x, y-25, text=name, tags=tag, font=("Arial", 10, "bold"))
        self.create_text(x, y+25, text=f"{value*1000:.1f}mH", tags=tag, font=("Arial", 9))
        
        # Terminaux
        self.create_line(x-40, y, x-20, y, width=2, tags=tag)
        self.create_line(x+20, y, x+40, y, width=2, tags=tag)
        self.create_oval(x-42, y-2, x-38, y+2, fill="red", outline="red", tags=tag)
        self.create_oval(x+38, y-2, x+42, y+2, fill="red", outline="red", tags=tag)
        
        return tag
    
    def draw_wire(self, wire):
        """Dessine un fil de connexion."""
        tag = f"wire_{wire.id}"
        self.create_line(wire.start_x, wire.start_y, wire.end_x, wire.end_y, 
                        fill="black", width=2, tags=tag)
        return tag
    
    def redraw_all(self):
        """Redessine tous les composants."""
        self.delete("all")
        self.draw_grid()
        
        # Dessiner d'abord les fils
        for wire in self.circuit_manager.get_all_wires():
            self.draw_component(wire)
        
        # Puis les composants
        for component in self.circuit_manager.get_all_components():
            self.draw_component(component)
    
    def on_click(self, event):
        """Gestion du clic gauche."""
        # Si on est en mode placement de composant
        if self.component_to_place:
            x, y = self.snap_position(event.x, event.y)
            self.add_component(self.component_to_place, x, y)
            # Réinitialiser le mode placement
            self.component_to_place = None
            self.config(cursor="")
            return
        
        # Si on est en mode création de fil
        if self.drawing_wire:
            # Chercher un composant à la position cliquée
            clicked_comp = self.find_component_at(event.x, event.y)
            
            if clicked_comp:
                if not self.wire_start:
                    # Premier clic - commencer le fil
                    self.wire_start = (clicked_comp, event.x, event.y)
                    # Créer une ligne temporaire
                    self.temp_wire_id = self.create_line(
                        event.x, event.y, event.x, event.y,
                        fill='yellow', width=2, dash=(5, 5), tags='temp_wire'
                    )
                else:
                    # Deuxième clic - terminer le fil
                    start_comp = self.wire_start[0]
                    if clicked_comp != start_comp:
                        # Créer le fil entre deux composants différents
                        self.create_wire(start_comp, clicked_comp)
                    # Si même composant, juste annuler le fil
                    
                    # Nettoyer dans tous les cas
                    if self.temp_wire_id:
                        self.delete(self.temp_wire_id)
                        self.temp_wire_id = None
                    self.wire_start = None
                    self.drawing_wire = False
                    self.config(cursor="")
            return
        
        # Vérifier si on a cliqué sur un composant pour le déplacer
        item = self.find_closest(event.x, event.y)[0]
        tags = self.gettags(item)
        
        if tags and tags[0].startswith("comp_"):
            comp_name = tags[0].replace("comp_", "")
            # Trouver le composant
            for comp in self.circuit_manager.get_all_components():
                if comp.name == comp_name:
                    self.selected_component = comp
                    self.drag_data["x"] = event.x
                    self.drag_data["y"] = event.y
                    self.drag_data["item"] = comp
                    break
    
    def on_drag(self, event):
        """Gestion du déplacement."""
        # Si on dessine un fil temporaire, mettre à jour la ligne
        if self.drawing_wire and self.wire_start and self.temp_wire_id:
            start_x, start_y = self.wire_start[1], self.wire_start[2]
            self.coords(self.temp_wire_id, start_x, start_y, event.x, event.y)
            return
        
        # Sinon, déplacer le composant si on en a un
        if self.drag_data["item"]:
            # Calculer le déplacement
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            
            # Mettre à jour la position du composant
            comp = self.drag_data["item"]
            comp.x += dx
            comp.y += dy
            
            # Mettre à jour les fils connectés à ce composant
            self.update_connected_wires(comp)
            
            # Redessiner
            self.draw_component(comp)
            
            # Mettre à jour pour le prochain déplacement
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
    
    def on_release(self, event):
        """Gestion du relâchement du bouton."""
        self.drag_data = {"x": 0, "y": 0, "item": None}
    
    def on_right_click(self, event):
        """Gestion du clic droit (menu contextuel)."""
        # Trouver le composant sous le curseur
        item = self.find_closest(event.x, event.y)[0]
        tags = self.gettags(item)
        
        if tags and tags[0].startswith("comp_"):
            comp_name = tags[0].replace("comp_", "")
            for comp in self.circuit_manager.get_all_components():
                if comp.name == comp_name:
                    self.selected_component = comp
                    # Émettre un événement pour le panneau de propriétés
                    self.event_generate("<<ComponentSelected>>")
                    break
    
    def clear_canvas(self):
        """Efface tout le canvas."""
        self.delete("all")
        self.draw_grid()
        self.selected_component = None
    
    def find_component_at(self, x, y):
        """
        Trouve le composant à la position donnée.
        
        Args:
            x, y: Coordonnées
            
        Returns:
            Composant trouvé ou None
        """
        # Chercher l'élément le plus proche
        item = self.find_closest(x, y)[0]
        tags = self.gettags(item)
        
        if tags and tags[0].startswith("comp_"):
            comp_name = tags[0].replace("comp_", "")
            # Trouver le composant dans le circuit manager
            for comp in self.circuit_manager.get_all_components():
                if comp.name == comp_name:
                    # Vérifier que le clic est assez proche
                    distance = ((comp.x - x) ** 2 + (comp.y - y) ** 2) ** 0.5
                    if distance < self.COMPONENT_CLICK_TOLERANCE:
                        return comp
        return None
    
    def create_wire(self, start_comp, end_comp):
        """
        Crée un fil entre deux composants.
        
        Args:
            start_comp: Composant de départ
            end_comp: Composant d'arrivée
        """
        from components import Wire
        
        # Créer le fil
        wire = Wire(
            x=start_comp.x,
            y=start_comp.y,
            start_comp=start_comp,
            end_comp=end_comp
        )
        wire.set_endpoints(start_comp.x, start_comp.y, end_comp.x, end_comp.y)
        
        # Ajouter au circuit manager
        self.circuit_manager.add_component(wire)
        
        # Connecter les composants
        start_comp.connect_to(end_comp)
        end_comp.connect_to(start_comp)
        
        # Dessiner le fil
        self.draw_component(wire)
    
    def update_connected_wires(self, component):
        """
        Met à jour les positions des fils connectés à un composant.
        
        Args:
            component: Composant qui a été déplacé
        """
        # Chercher tous les fils connectés à ce composant
        for wire in self.circuit_manager.get_all_wires():
            if isinstance(wire, Wire):
                needs_update = False
                
                # Mettre à jour le point de départ si c'est le composant de départ
                if wire.start_component == component:
                    wire.start_x = component.x
                    wire.start_y = component.y
                    needs_update = True
                
                # Mettre à jour le point d'arrivée si c'est le composant d'arrivée
                if wire.end_component == component:
                    wire.end_x = component.x
                    wire.end_y = component.y
                    needs_update = True
                
                # Redessiner le fil si nécessaire
                if needs_update:
                    self.draw_component(wire)
