"""
Composant Source de Tension.
"""
from components.base_component import BaseComponent


class VoltageSource(BaseComponent):
    """Classe représentant une source de tension DC."""
    
    def __init__(self, x=0, y=0, name=None, value=12):
        """
        Initialise une source de tension.
        
        Args:
            x (int): Position X
            y (int): Position Y
            name (str): Nom (ex: V1)
            value (float): Tension en Volts (défaut: 12V)
        """
        super().__init__(x, y, name, value)
        self.polarity = "+"  # Polarité positive par défaut
    
    def get_prefix(self):
        """Préfixe pour les sources de tension."""
        return "V"
    
    def get_default_value(self):
        """Valeur par défaut: 12V."""
        return 12
    
    def get_unit(self):
        """Unité: Volt."""
        return "V"
    
    def get_symbol_name(self):
        """Nom du symbole."""
        return "Voltage Source"
    
    def to_dict(self):
        """Convertit en dictionnaire avec polarité."""
        data = super().to_dict()
        data['polarity'] = self.polarity
        return data
    
    @classmethod
    def from_dict(cls, data):
        """Crée depuis un dictionnaire."""
        comp = super().from_dict(data)
        if 'polarity' in data:
            comp.polarity = data['polarity']
        return comp
