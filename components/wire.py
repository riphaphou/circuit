"""
Composant Fil de connexion.
"""
from components.base_component import BaseComponent


class Wire(BaseComponent):
    """Classe représentant un fil de connexion entre composants."""
    
    def __init__(self, x=0, y=0, name=None, start_comp=None, end_comp=None):
        """
        Initialise un fil.
        
        Args:
            x (int): Position X
            y (int): Position Y
            name (str): Nom (ex: W1)
            start_comp: Composant de départ
            end_comp: Composant d'arrivée
        """
        super().__init__(x, y, name, value=0)
        self.start_component = start_comp
        self.end_component = end_comp
        self.start_x = x
        self.start_y = y
        self.end_x = x
        self.end_y = y
    
    def get_prefix(self):
        """Préfixe pour les fils."""
        return "W"
    
    def get_default_value(self):
        """Les fils n'ont pas de valeur."""
        return 0
    
    def get_unit(self):
        """Les fils n'ont pas d'unité."""
        return ""
    
    def get_symbol_name(self):
        """Nom du symbole."""
        return "Wire"
    
    def set_endpoints(self, x1, y1, x2, y2):
        """
        Définit les extrémités du fil.
        
        Args:
            x1, y1: Coordonnées du point de départ
            x2, y2: Coordonnées du point d'arrivée
        """
        self.start_x = x1
        self.start_y = y1
        self.end_x = x2
        self.end_y = y2
    
    def to_dict(self):
        """Convertit en dictionnaire."""
        data = super().to_dict()
        data['start_x'] = self.start_x
        data['start_y'] = self.start_y
        data['end_x'] = self.end_x
        data['end_y'] = self.end_y
        if self.start_component:
            data['start_component_id'] = self.start_component.id if hasattr(self.start_component, 'id') else None
        if self.end_component:
            data['end_component_id'] = self.end_component.id if hasattr(self.end_component, 'id') else None
        return data
    
    @classmethod
    def from_dict(cls, data):
        """Crée depuis un dictionnaire."""
        wire = cls(x=data['x'], y=data['y'], name=data['name'])
        wire.id = data['id']
        wire.start_x = data.get('start_x', 0)
        wire.start_y = data.get('start_y', 0)
        wire.end_x = data.get('end_x', 0)
        wire.end_y = data.get('end_y', 0)
        return wire
