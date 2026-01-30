# -*- coding: utf-8 -*-
"""
Gestionnaire du circuit électronique
"""

from core.components import Resistor, Battery, LED, Switch, Wire

class CircuitManager:
    """Gestionnaire centralisé du circuit"""
    
    def __init__(self):
        self.components = {}  # {id: Component}
        self.wires = {}  # {id: Wire}
        self.next_component_id = 1
        self.next_wire_id = 1
        
    def add_component(self, component_type, x, y, **kwargs):
        """Ajoute un composant au circuit"""
        comp_id = self.next_component_id
        self.next_component_id += 1
        
        if component_type == "resistor":
            component = Resistor(x, y, comp_id, kwargs.get('value', 1000))
        elif component_type == "battery":
            component = Battery(x, y, comp_id, kwargs.get('voltage', 9))
        elif component_type == "led":
            component = LED(x, y, comp_id)
        elif component_type == "switch":
            component = Switch(x, y, comp_id, kwargs.get('closed', True))
        else:
            return None
            
        self.components[comp_id] = component
        return component
        
    def remove_component(self, comp_id):
        """Supprime un composant et ses fils associés"""
        if comp_id in self.components:
            # Supprimer tous les fils connectés à ce composant
            wires_to_remove = []
            for wire_id, wire in self.wires.items():
                if wire.comp1_id == comp_id or wire.comp2_id == comp_id:
                    wires_to_remove.append(wire_id)
            for wire_id in wires_to_remove:
                del self.wires[wire_id]
            # Supprimer le composant
            del self.components[comp_id]
            return True
        return False
        
    def add_wire(self, comp1_id, pin1, comp2_id, pin2):
        """Ajoute un fil de connexion entre deux composants"""
        # Validation : ne pas connecter un composant à lui-même
        if comp1_id == comp2_id:
            return None
            
        wire_id = self.next_wire_id
        self.next_wire_id += 1
        
        wire = Wire(wire_id, comp1_id, pin1, comp2_id, pin2)
        self.wires[wire_id] = wire
        return wire
        
    def remove_wire(self, wire_id):
        """Supprime un fil"""
        if wire_id in self.wires:
            del self.wires[wire_id]
            return True
        return False
        
    def get_component_at(self, x, y):
        """Retourne le composant à la position (x, y)"""
        for comp_id, component in self.components.items():
            if component.contains_point(x, y):
                return component
        return None
        
    def calculate_circuit(self):
        """Calcule les valeurs du circuit (courant, tension, etc.)"""
        # TODO: Implémenter les calculs de circuit (loi d'Ohm, loi de Kirchhoff)
        # Pour l'instant, retourne des valeurs fictives
        results = {
            'total_resistance': sum(c.value for c in self.components.values() 
                                   if isinstance(c, Resistor)),
            'voltage': sum(c.voltage for c in self.components.values() 
                          if isinstance(c, Battery)),
            'current': 0,
        }
        if results['total_resistance'] > 0 and results['voltage'] > 0:
            results['current'] = results['voltage'] / results['total_resistance']
        return results
        
    def clear(self):
        """Efface tout le circuit"""
        self.components.clear()
        self.wires.clear()
        self.next_component_id = 1
        self.next_wire_id = 1
