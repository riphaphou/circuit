"""
Composant Inductance.
"""
from components.base_component import BaseComponent


class Inductor(BaseComponent):
    """Classe représentant une inductance."""
    
    def __init__(self, x=0, y=0, name=None, value=0.001):
        """
        Initialise une inductance.
        
        Args:
            x (int): Position X
            y (int): Position Y
            name (str): Nom (ex: L1)
            value (float): Inductance en Henrys (défaut: 1mH)
        """
        super().__init__(x, y, name, value)
    
    def get_prefix(self):
        """Préfixe pour les inductances."""
        return "L"
    
    def get_default_value(self):
        """Valeur par défaut: 1mH."""
        return 0.001
    
    def get_unit(self):
        """Unité: Henry."""
        return "H"
    
    def get_symbol_name(self):
        """Nom du symbole."""
        return "Inductor"
