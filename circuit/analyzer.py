"""
Analyseur de topologie de circuit.
"""
from components import Resistor, VoltageSource, CurrentSource


class CircuitAnalyzer:
    """Analyse la topologie et la structure du circuit."""
    
    def __init__(self, circuit_manager):
        """
        Initialise l'analyseur.
        
        Args:
            circuit_manager: Gestionnaire de circuit à analyser
        """
        self.circuit_manager = circuit_manager
    
    def detect_series_resistors(self):
        """
        Détecte les résistances en série.
        
        Returns:
            Liste de groupes de résistances en série
        """
        resistors = self.circuit_manager.get_resistors()
        # Implémentation simplifiée: considère que toutes les résistances
        # sans branchement sont en série
        if len(resistors) >= 2:
            return [resistors]
        return []
    
    def detect_parallel_resistors(self):
        """
        Détecte les résistances en parallèle.
        
        Returns:
            Liste de groupes de résistances en parallèle
        """
        # Implémentation simplifiée
        return []
    
    def get_circuit_type(self):
        """
        Détermine le type de circuit (série, parallèle, mixte).
        
        Returns:
            str: 'series', 'parallel', 'mixed', ou 'unknown'
        """
        resistors = self.circuit_manager.get_resistors()
        if len(resistors) == 0:
            return 'unknown'
        elif len(resistors) == 1:
            return 'simple'
        else:
            # Analyse simplifiée basée sur les connexions
            series = self.detect_series_resistors()
            parallel = self.detect_parallel_resistors()
            
            if series and not parallel:
                return 'series'
            elif parallel and not series:
                return 'parallel'
            elif series and parallel:
                return 'mixed'
            else:
                return 'unknown'
    
    def get_nodes(self):
        """
        Identifie les nœuds du circuit.
        
        Returns:
            Liste des nœuds (positions de connexion)
        """
        nodes = []
        # Analyser les connexions via les fils
        for wire in self.circuit_manager.get_all_wires():
            if wire.start_component:
                nodes.append((wire.start_x, wire.start_y))
            if wire.end_component:
                nodes.append((wire.end_x, wire.end_y))
        
        # Supprimer les doublons
        return list(set(nodes))
    
    def is_circuit_valid(self):
        """
        Vérifie si le circuit est valide pour l'analyse.
        
        Returns:
            tuple: (bool, str) - (valide, message d'erreur)
        """
        components = self.circuit_manager.get_all_components()
        
        if len(components) == 0:
            return False, "Circuit vide"
        
        # Vérifier qu'il y a au moins une source
        sources = self.circuit_manager.get_voltage_sources() + \
                  self.circuit_manager.get_current_sources()
        
        if len(sources) == 0:
            return False, "Aucune source de tension ou courant"
        
        # Vérifier les valeurs nulles
        for comp in components:
            if isinstance(comp, Resistor) and comp.value <= 0:
                return False, f"Résistance {comp.name} a une valeur invalide"
        
        return True, "Circuit valide"
    
    def get_circuit_info(self):
        """
        Retourne des informations sur le circuit.
        
        Returns:
            dict: Informations du circuit
        """
        return {
            'num_components': len(self.circuit_manager.components),
            'num_wires': len(self.circuit_manager.wires),
            'num_resistors': len(self.circuit_manager.get_resistors()),
            'num_voltage_sources': len(self.circuit_manager.get_voltage_sources()),
            'num_current_sources': len(self.circuit_manager.get_current_sources()),
            'circuit_type': self.get_circuit_type(),
            'valid': self.is_circuit_valid()
        }
