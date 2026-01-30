"""
Composant Source de Courant.
"""
from components.base_component import BaseComponent


class CurrentSource(BaseComponent):
    """Classe représentant une source de courant DC."""
    
    def __init__(self, x=0, y=0, name=None, value=0.001):
        """
        Initialise une source de courant.
        
        Args:
            x (int): Position X
            y (int): Position Y
            name (str): Nom (ex: I1)
            value (float): Courant en Ampères (défaut: 1mA)
        """
        super().__init__(x, y, name, value)
    
    def get_prefix(self):
        """Préfixe pour les sources de courant."""
        return "I"
    
    def get_default_value(self):
        """Valeur par défaut: 1mA."""
        return 0.001
    
    def get_unit(self):
        """Unité: Ampère."""
        return "A"
    
    def get_symbol_name(self):
        """Nom du symbole."""
        return "Current Source"
