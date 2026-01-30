# -*- coding: utf-8 -*-
"""
Classes de base pour les composants électroniques
"""

class Component:
    """Classe de base pour tous les composants électroniques"""
    
    def __init__(self, x, y, component_id):
        self.x = x
        self.y = y
        self.id = component_id
        self.canvas_items = []  # IDs des éléments canvas
        self.pins = []  # Positions des bornes [(x, y), ...]
        
    def draw(self, canvas, theme):
        """Dessine le composant sur le canvas"""
        raise NotImplementedError
        
    def get_nearest_pin(self, x, y):
        """Retourne la borne la plus proche du point (x, y)"""
        if not self.pins:
            return None
        min_dist = float('inf')
        nearest = None
        for px, py in self.pins:
            dist = ((px - x)**2 + (py - y)**2)**0.5
            if dist < min_dist:
                min_dist = dist
                nearest = (px, py)
        return nearest if min_dist < 30 else None
        
    def contains_point(self, x, y, threshold=20):
        """Vérifie si le point (x, y) est sur le composant"""
        return (abs(x - self.x) < threshold and 
                abs(y - self.y) < threshold)


class Resistor(Component):
    """Résistance"""
    
    def __init__(self, x, y, component_id, value=1000):
        super().__init__(x, y, component_id)
        self.value = value  # en ohms
        self.width = 60
        self.height = 20
        # Bornes aux extrémités gauche et droite
        self.pins = [(x - 40, y), (x + 40, y)]
        
    def draw(self, canvas, theme):
        """Dessine la résistance"""
        color = theme.get('component_color', '#000000')
        # Lignes de connexion
        canvas.create_line(self.x - 40, self.y, self.x - 20, self.y, 
                          fill=color, width=2, tags=f"component_{self.id}")
        canvas.create_line(self.x + 20, self.y, self.x + 40, self.y, 
                          fill=color, width=2, tags=f"component_{self.id}")
        # Rectangle de la résistance
        canvas.create_rectangle(self.x - 20, self.y - 10, 
                               self.x + 20, self.y + 10,
                               outline=color, width=2, fill="",
                               tags=f"component_{self.id}")
        # Label
        canvas.create_text(self.x, self.y + 25, 
                          text=f"{self.value}Ω",
                          fill=theme.get('text_color', '#000000'),
                          tags=f"component_{self.id}")


class Battery(Component):
    """Pile/Batterie"""
    
    def __init__(self, x, y, component_id, voltage=9):
        super().__init__(x, y, component_id)
        self.voltage = voltage  # en volts
        # Bornes en haut (positif) et en bas (négatif)
        self.pins = [(x, y - 30), (x, y + 30)]
        
    def draw(self, canvas, theme):
        """Dessine la batterie"""
        color = theme.get('component_color', '#000000')
        # Ligne du haut (pôle positif)
        canvas.create_line(self.x - 15, self.y - 20, self.x + 15, self.y - 20,
                          fill=color, width=3, tags=f"component_{self.id}")
        # Ligne du bas (pôle négatif) - plus courte
        canvas.create_line(self.x - 10, self.y + 20, self.x + 10, self.y + 20,
                          fill=color, width=3, tags=f"component_{self.id}")
        # Lignes de connexion
        canvas.create_line(self.x, self.y - 30, self.x, self.y - 20,
                          fill=color, width=2, tags=f"component_{self.id}")
        canvas.create_line(self.x, self.y + 20, self.x, self.y + 30,
                          fill=color, width=2, tags=f"component_{self.id}")
        # Symboles + et -
        canvas.create_text(self.x + 25, self.y - 20, text="+", 
                          fill=color, font=("Arial", 14, "bold"),
                          tags=f"component_{self.id}")
        canvas.create_text(self.x + 25, self.y + 20, text="-", 
                          fill=color, font=("Arial", 14, "bold"),
                          tags=f"component_{self.id}")
        # Label
        canvas.create_text(self.x, self.y, text=f"{self.voltage}V",
                          fill=theme.get('text_color', '#000000'),
                          tags=f"component_{self.id}")


class LED(Component):
    """LED (Diode électroluminescente)"""
    
    def __init__(self, x, y, component_id):
        super().__init__(x, y, component_id)
        # Bornes aux extrémités
        self.pins = [(x - 30, y), (x + 30, y)]
        
    def draw(self, canvas, theme):
        """Dessine la LED"""
        color = theme.get('component_color', '#000000')
        # Lignes de connexion
        canvas.create_line(self.x - 30, self.y, self.x - 15, self.y,
                          fill=color, width=2, tags=f"component_{self.id}")
        canvas.create_line(self.x + 15, self.y, self.x + 30, self.y,
                          fill=color, width=2, tags=f"component_{self.id}")
        # Triangle de la LED
        canvas.create_polygon(self.x - 15, self.y - 10,
                             self.x - 15, self.y + 10,
                             self.x + 5, self.y,
                             outline=color, fill="", width=2,
                             tags=f"component_{self.id}")
        # Barre verticale
        canvas.create_line(self.x + 5, self.y - 10, self.x + 5, self.y + 10,
                          fill=color, width=2, tags=f"component_{self.id}")
        # Label
        canvas.create_text(self.x, self.y + 25, text="LED",
                          fill=theme.get('text_color', '#000000'),
                          tags=f"component_{self.id}")


class Switch(Component):
    """Interrupteur"""
    
    def __init__(self, x, y, component_id, closed=True):
        super().__init__(x, y, component_id)
        self.closed = closed
        self.pins = [(x - 30, y), (x + 30, y)]
        
    def draw(self, canvas, theme):
        """Dessine l'interrupteur"""
        color = theme.get('component_color', '#000000')
        # Bornes
        canvas.create_oval(self.x - 32, self.y - 2, self.x - 28, self.y + 2,
                          fill=color, tags=f"component_{self.id}")
        canvas.create_oval(self.x + 28, self.y - 2, self.x + 32, self.y + 2,
                          fill=color, tags=f"component_{self.id}")
        # Ligne de l'interrupteur
        if self.closed:
            canvas.create_line(self.x - 28, self.y, self.x + 28, self.y,
                              fill=color, width=2, tags=f"component_{self.id}")
        else:
            # Ouvert - ligne en diagonale
            canvas.create_line(self.x - 28, self.y, self.x + 15, self.y - 15,
                              fill=color, width=2, tags=f"component_{self.id}")
        # Label
        state = "ON" if self.closed else "OFF"
        canvas.create_text(self.x, self.y + 25, text=state,
                          fill=theme.get('text_color', '#000000'),
                          tags=f"component_{self.id}")


class Wire:
    """Fil de connexion entre deux composants"""
    
    def __init__(self, wire_id, comp1_id, pin1, comp2_id, pin2):
        self.id = wire_id
        self.comp1_id = comp1_id
        self.pin1 = pin1  # (x, y)
        self.comp2_id = comp2_id
        self.pin2 = pin2  # (x, y)
        self.canvas_item = None
        
    def draw(self, canvas, theme):
        """Dessine le fil"""
        color = theme.get('wire_color', '#FF0000')
        self.canvas_item = canvas.create_line(
            self.pin1[0], self.pin1[1],
            self.pin2[0], self.pin2[1],
            fill=color, width=2, tags=f"wire_{self.id}"
        )
        return self.canvas_item
