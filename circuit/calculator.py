"""
Moteur de calculs électriques.
"""
import numpy as np
from components import Resistor, VoltageSource, CurrentSource


class CircuitCalculator:
    """Effectue les calculs électriques sur le circuit."""
    
    def __init__(self, circuit_manager):
        """
        Initialise le calculateur.
        
        Args:
            circuit_manager: Gestionnaire de circuit
        """
        self.circuit_manager = circuit_manager
        self.results = {}
    
    def calculate_ohms_law(self, voltage=None, current=None, resistance=None):
        """
        Applique la loi d'Ohm: V = R × I
        
        Args:
            voltage: Tension (V)
            current: Courant (A)
            resistance: Résistance (Ω)
            
        Returns:
            dict: Résultats avec la valeur manquante calculée
        """
        if voltage is not None and current is not None:
            # Calculer R
            if current != 0:
                resistance = voltage / current
            else:
                resistance = float('inf')
        elif voltage is not None and resistance is not None:
            # Calculer I
            if resistance != 0:
                current = voltage / resistance
            else:
                current = float('inf')
        elif current is not None and resistance is not None:
            # Calculer V
            voltage = resistance * current
        
        return {
            'voltage': voltage,
            'current': current,
            'resistance': resistance
        }
    
    def calculate_power(self, voltage=None, current=None, resistance=None):
        """
        Calcule la puissance: P = V × I = R × I² = V²/R
        
        Args:
            voltage: Tension (V)
            current: Courant (A)
            resistance: Résistance (Ω)
            
        Returns:
            float: Puissance en Watts
        """
        if voltage is not None and current is not None:
            return voltage * current
        elif resistance is not None and current is not None:
            return resistance * current * current
        elif voltage is not None and resistance is not None:
            if resistance != 0:
                return (voltage * voltage) / resistance
        return 0
    
    def calculate_series_resistance(self, resistances):
        """
        Calcule la résistance équivalente en série: Req = R1 + R2 + ... + Rn
        
        Args:
            resistances: Liste de valeurs de résistances
            
        Returns:
            float: Résistance équivalente
        """
        return sum(resistances)
    
    def calculate_parallel_resistance(self, resistances):
        """
        Calcule la résistance équivalente en parallèle: 1/Req = 1/R1 + 1/R2 + ... + 1/Rn
        
        Args:
            resistances: Liste de valeurs de résistances
            
        Returns:
            float: Résistance équivalente
        """
        if not resistances:
            return 0
        
        # Filtrer les résistances nulles
        valid_resistances = [r for r in resistances if r > 0]
        if not valid_resistances:
            return 0
        
        reciprocal_sum = sum(1/r for r in valid_resistances)
        if reciprocal_sum > 0:
            return 1 / reciprocal_sum
        return 0
    
    def calculate_voltage_divider(self, vin, r1, r2):
        """
        Calcule le diviseur de tension: Vout = Vin × (R2 / (R1 + R2))
        
        Args:
            vin: Tension d'entrée
            r1: Résistance 1
            r2: Résistance 2
            
        Returns:
            float: Tension de sortie
        """
        total_r = r1 + r2
        if total_r > 0:
            return vin * (r2 / total_r)
        return 0
    
    def calculate_current_divider(self, itotal, r1, r2):
        """
        Calcule le diviseur de courant: I1 = Itotal × (R2 / (R1 + R2))
        
        Args:
            itotal: Courant total
            r1: Résistance 1
            r2: Résistance 2
            
        Returns:
            float: Courant dans R1
        """
        total_r = r1 + r2
        if total_r > 0:
            return itotal * (r2 / total_r)
        return 0
    
    def calculate_millman_theorem(self, voltages, resistances, currents=None):
        """
        Applique le théorème de Millman: V_noeud = (Σ(Ei/Ri) + Σ(Ij)) / Σ(1/Ri)
        
        Args:
            voltages: Liste de tensions des sources
            resistances: Liste de résistances
            currents: Liste de sources de courant (optionnel)
            
        Returns:
            float: Tension au nœud
        """
        if not resistances or len(voltages) != len(resistances):
            return 0
        
        # Filtrer les résistances nulles
        valid_pairs = [(v, r) for v, r in zip(voltages, resistances) if r > 0]
        if not valid_pairs:
            return 0
        
        voltages, resistances = zip(*valid_pairs)
        
        # Calculer la somme des conductances
        conductance_sum = sum(1/r for r in resistances)
        
        # Calculer la somme pondérée des tensions
        voltage_sum = sum(v/r for v, r in zip(voltages, resistances))
        
        # Ajouter les sources de courant si présentes
        if currents:
            current_sum = sum(currents)
            voltage_sum += current_sum
        
        if conductance_sum > 0:
            return voltage_sum / conductance_sum
        return 0
    
    def analyze_circuit(self):
        """
        Analyse complète du circuit et calcule toutes les grandeurs.
        
        Returns:
            dict: Résultats de l'analyse
        """
        results = {
            'total_voltage': 0,
            'total_current': 0,
            'total_power': 0,
            'equivalent_resistance': 0,
            'components': {}
        }
        
        # Récupérer les composants
        resistors = self.circuit_manager.get_resistors()
        voltage_sources = self.circuit_manager.get_voltage_sources()
        current_sources = self.circuit_manager.get_current_sources()
        
        if not resistors:
            return results
        
        # Calculer la résistance équivalente (suppose série pour simplifier)
        resistance_values = [r.value for r in resistors]
        req = self.calculate_series_resistance(resistance_values)
        results['equivalent_resistance'] = req
        
        # Calculer tension et courant totaux
        if voltage_sources:
            total_voltage = sum(v.value for v in voltage_sources)
            results['total_voltage'] = total_voltage
            
            if req > 0:
                results['total_current'] = total_voltage / req
                results['total_power'] = self.calculate_power(
                    total_voltage, 
                    results['total_current'], 
                    req
                )
        
        # Calculer pour chaque composant
        for resistor in resistors:
            if req > 0 and results['total_current'] > 0:
                voltage = resistor.value * results['total_current']
                power = self.calculate_power(
                    voltage, 
                    results['total_current'], 
                    resistor.value
                )
                
                results['components'][resistor.name] = {
                    'voltage': voltage,
                    'current': results['total_current'],
                    'power': power,
                    'resistance': resistor.value
                }
        
        self.results = results
        return results
    
    def format_results(self):
        """
        Formate les résultats pour l'affichage.
        
        Returns:
            str: Résultats formatés
        """
        if not self.results:
            return "Aucun résultat de calcul disponible."
        
        output = []
        output.append("=== Résultats des calculs ===\n")
        
        if self.results.get('total_voltage'):
            output.append(f"Tension totale: {self.results['total_voltage']:.3f} V")
        
        if self.results.get('total_current'):
            output.append(f"Courant total: {self.results['total_current']:.6f} A")
        
        if self.results.get('total_power'):
            output.append(f"Puissance totale: {self.results['total_power']:.6f} W")
        
        if self.results.get('equivalent_resistance'):
            output.append(f"Résistance équivalente: {self.results['equivalent_resistance']:.3f} Ω")
        
        if self.results.get('components'):
            output.append("\n--- Composants ---")
            for name, values in self.results['components'].items():
                output.append(f"\n{name}:")
                output.append(f"  Tension: {values.get('voltage', 0):.3f} V")
                output.append(f"  Courant: {values.get('current', 0):.6f} A")
                output.append(f"  Puissance: {values.get('power', 0):.6f} W")
        
        return '\n'.join(output)
