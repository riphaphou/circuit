"""
Classe de base pour tous les composants électroniques.
"""

class BaseComponent:
    """Classe de base pour tous les composants du circuit."""
    
    component_counter = 0
    
    def __init__(self, x=0, y=0, name=None, value=None):
        """
        Initialise un composant de base.
        
        Args:
            x (int): Position X sur le canvas
            y (int): Position Y sur le canvas
            name (str): Nom du composant (ex: R1, V1)
            value (float): Valeur du composant (résistance, tension, etc.)
        """
        BaseComponent.component_counter += 1
        self.id = BaseComponent.component_counter
        self.x = x
        self.y = y
        self.name = name if name else f"{self.get_prefix()}{self.id}"
        self.value = value if value is not None else self.get_default_value()
        self.connections = []  # Liste des nœuds/composants connectés
        self.canvas_id = None  # ID du dessin sur le canvas Tkinter
        self.selected = False
        
    def get_prefix(self):
        """Retourne le préfixe du nom du composant (R, V, C, etc.)."""
        return "C"
    
    def get_default_value(self):
        """Retourne la valeur par défaut du composant."""
        return 0
    
    def get_unit(self):
        """Retourne l'unité du composant."""
        return ""
    
    def get_symbol_name(self):
        """Retourne le nom du symbole pour l'affichage."""
        return "Component"
    
    def connect_to(self, other):
        """
        Connecte ce composant à un autre.
        
        Args:
            other: Autre composant ou nœud
        """
        if other not in self.connections:
            self.connections.append(other)
    
    def disconnect_from(self, other):
        """
        Déconnecte ce composant d'un autre.
        
        Args:
            other: Composant ou nœud à déconnecter
        """
        if other in self.connections:
            self.connections.remove(other)
    
    def to_dict(self):
        """Convertit le composant en dictionnaire pour la sauvegarde JSON."""
        return {
            'type': self.__class__.__name__,
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'x': self.x,
            'y': self.y,
            'connections': [c.id if hasattr(c, 'id') else c for c in self.connections]
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crée un composant à partir d'un dictionnaire."""
        comp = cls(x=data['x'], y=data['y'], name=data['name'], value=data['value'])
        comp.id = data['id']
        return comp
    
    def __str__(self):
        """Représentation textuelle du composant."""
        return f"{self.name}: {self.value}{self.get_unit()}"
    
    def __repr__(self):
        """Représentation pour le débogage."""
        return f"<{self.__class__.__name__} {self.name} at ({self.x}, {self.y})>"
