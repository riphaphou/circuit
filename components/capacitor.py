"""
Composant Condensateur.
"""
from components.base_component import BaseComponent


class Capacitor(BaseComponent):
    """Classe représentant un condensateur."""
    
    def __init__(self, x=0, y=0, name=None, value=0.000001):
        """
        Initialise un condensateur.
        
        Args:
            x (int): Position X
            y (int): Position Y
            name (str): Nom (ex: C1)
            value (float): Capacité en Farads (défaut: 1µF)
        """
        super().__init__(x, y, name, value)
    
    def get_prefix(self):
        """Préfixe pour les condensateurs."""
        return "C"
    
    def get_default_value(self):
        """Valeur par défaut: 1µF."""
        return 0.000001
    
    def get_unit(self):
        """Unité: Farad."""
        return "F"
    
    def get_symbol_name(self):
        """Nom du symbole."""
        return "Capacitor"
