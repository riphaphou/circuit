"""
Gestionnaire du circuit électronique.
"""
from components import *


class CircuitManager:
    """Gère la liste des composants et les connexions du circuit."""
    
    def __init__(self):
        """Initialise un gestionnaire de circuit vide."""
        self.components = []
        self.wires = []
        self.nodes = {}  # Dictionnaire des nœuds de connexion
        
    def add_component(self, component):
        """
        Ajoute un composant au circuit.
        
        Args:
            component: Composant à ajouter
        """
        if isinstance(component, Wire):
            self.wires.append(component)
        else:
            self.components.append(component)
    
    def remove_component(self, component):
        """
        Supprime un composant du circuit.
        
        Args:
            component: Composant à supprimer
        """
        if component in self.components:
            self.components.remove(component)
        elif component in self.wires:
            self.wires.remove(component)
    
    def get_component_by_id(self, comp_id):
        """
        Trouve un composant par son ID.
        
        Args:
            comp_id (int): ID du composant
            
        Returns:
            Composant trouvé ou None
        """
        for comp in self.components + self.wires:
            if comp.id == comp_id:
                return comp
        return None
    
    def get_component_at_position(self, x, y, tolerance=20):
        """
        Trouve un composant à une position donnée.
        
        Args:
            x, y: Coordonnées
            tolerance: Distance maximale en pixels
            
        Returns:
            Composant trouvé ou None
        """
        for comp in self.components:
            if abs(comp.x - x) <= tolerance and abs(comp.y - y) <= tolerance:
                return comp
        return None
    
    def clear(self):
        """Efface tous les composants du circuit."""
        self.components.clear()
        self.wires.clear()
        self.nodes.clear()
    
    def get_resistors(self):
        """Retourne la liste des résistances."""
        return [c for c in self.components if isinstance(c, Resistor)]
    
    def get_voltage_sources(self):
        """Retourne la liste des sources de tension."""
        return [c for c in self.components if isinstance(c, VoltageSource)]
    
    def get_current_sources(self):
        """Retourne la liste des sources de courant."""
        return [c for c in self.components if isinstance(c, CurrentSource)]
    
    def get_all_components(self):
        """Retourne tous les composants (sans les fils)."""
        return self.components.copy()
    
    def get_all_wires(self):
        """Retourne tous les fils."""
        return self.wires.copy()
    
    def to_dict(self):
        """Convertit le circuit en dictionnaire pour sauvegarde."""
        return {
            'components': [c.to_dict() for c in self.components],
            'wires': [w.to_dict() for w in self.wires]
        }
    
    def from_dict(self, data):
        """
        Charge un circuit depuis un dictionnaire.
        
        Args:
            data: Dictionnaire contenant les données du circuit
        """
        self.clear()
        
        # Mapping des types de composants
        component_types = {
            'Resistor': Resistor,
            'VoltageSource': VoltageSource,
            'CurrentSource': CurrentSource,
            'Capacitor': Capacitor,
            'Inductor': Inductor,
            'Wire': Wire
        }
        
        # Charger les composants
        id_mapping = {}
        for comp_data in data.get('components', []):
            comp_type = component_types.get(comp_data['type'])
            if comp_type:
                comp = comp_type.from_dict(comp_data)
                self.add_component(comp)
                id_mapping[comp_data['id']] = comp
        
        # Charger les fils
        for wire_data in data.get('wires', []):
            wire = Wire.from_dict(wire_data)
            # Reconnecter les composants
            if 'start_component_id' in wire_data and wire_data['start_component_id']:
                wire.start_component = id_mapping.get(wire_data['start_component_id'])
            if 'end_component_id' in wire_data and wire_data['end_component_id']:
                wire.end_component = id_mapping.get(wire_data['end_component_id'])
            self.add_component(wire)
    
    def __str__(self):
        """Représentation textuelle du circuit."""
        return f"Circuit: {len(self.components)} composants, {len(self.wires)} fils"
