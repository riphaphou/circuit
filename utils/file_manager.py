"""
Gestionnaire de fichiers pour sauvegarder et charger les circuits.
"""
import json
import os


class FileManager:
    """Gère la sauvegarde et le chargement des circuits en JSON."""
    
    @staticmethod
    def save_circuit(circuit_manager, filepath):
        """
        Sauvegarde un circuit dans un fichier JSON.
        
        Args:
            circuit_manager: Gestionnaire de circuit à sauvegarder
            filepath: Chemin du fichier de destination
            
        Returns:
            bool: True si sauvegarde réussie, False sinon
        """
        try:
            data = circuit_manager.to_dict()
            
            # Créer le répertoire si nécessaire
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            # Écrire le fichier JSON
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
            return False
    
    @staticmethod
    def load_circuit(circuit_manager, filepath):
        """
        Charge un circuit depuis un fichier JSON.
        
        Args:
            circuit_manager: Gestionnaire de circuit à remplir
            filepath: Chemin du fichier source
            
        Returns:
            bool: True si chargement réussi, False sinon
        """
        try:
            if not os.path.exists(filepath):
                print(f"Fichier non trouvé: {filepath}")
                return False
            
            # Lire le fichier JSON
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Charger les données dans le circuit
            circuit_manager.from_dict(data)
            
            return True
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")
            return False
    
    @staticmethod
    def get_example_circuits():
        """
        Retourne une liste de circuits d'exemple.
        
        Returns:
            dict: Dictionnaire de circuits d'exemple
        """
        return {
            'simple_circuit': {
                'name': 'Circuit simple (série)',
                'description': 'Une source de tension et deux résistances en série',
                'data': {
                    'components': [
                        {
                            'type': 'VoltageSource',
                            'id': 1,
                            'name': 'V1',
                            'value': 12,
                            'x': 100,
                            'y': 100,
                            'connections': [],
                            'polarity': '+'
                        },
                        {
                            'type': 'Resistor',
                            'id': 2,
                            'name': 'R1',
                            'value': 1000,
                            'x': 250,
                            'y': 100,
                            'connections': []
                        },
                        {
                            'type': 'Resistor',
                            'id': 3,
                            'name': 'R2',
                            'value': 2000,
                            'x': 400,
                            'y': 100,
                            'connections': []
                        }
                    ],
                    'wires': []
                }
            },
            'voltage_divider': {
                'name': 'Diviseur de tension',
                'description': 'Circuit diviseur de tension classique',
                'data': {
                    'components': [
                        {
                            'type': 'VoltageSource',
                            'id': 1,
                            'name': 'V1',
                            'value': 9,
                            'x': 100,
                            'y': 150,
                            'connections': [],
                            'polarity': '+'
                        },
                        {
                            'type': 'Resistor',
                            'id': 2,
                            'name': 'R1',
                            'value': 4700,
                            'x': 250,
                            'y': 100,
                            'connections': []
                        },
                        {
                            'type': 'Resistor',
                            'id': 3,
                            'name': 'R2',
                            'value': 2200,
                            'x': 250,
                            'y': 200,
                            'connections': []
                        }
                    ],
                    'wires': []
                }
            }
        }
