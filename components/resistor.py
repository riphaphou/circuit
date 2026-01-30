"""
Composant Résistance.
"""
from components.base_component import BaseComponent


class Resistor(BaseComponent):
    """Classe représentant une résistance."""
    
    def __init__(self, x=0, y=0, name=None, value=1000):
        """
        Initialise une résistance.
        
        Args:
            x (int): Position X
            y (int): Position Y
            name (str): Nom (ex: R1)
            value (float): Résistance en Ohms (défaut: 1000Ω)
        """
        super().__init__(x, y, name, value)
    
    def get_prefix(self):
        """Préfixe pour les résistances."""
        return "R"
    
    def get_default_value(self):
        """Valeur par défaut: 1kΩ."""
        return 1000
    
    def get_unit(self):
        """Unité: Ohm."""
        return "Ω"
    
    def get_symbol_name(self):
        """Nom du symbole."""
        return "Resistor"
