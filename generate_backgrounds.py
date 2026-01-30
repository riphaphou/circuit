#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération d'images d'exemple pour les fonds de canvas
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_grid_pattern():
    """Crée un motif de grille technique"""
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Grille fine
    for i in range(0, 400, 20):
        draw.line([(i, 0), (i, 400)], fill='#E0E0E0', width=1)
        draw.line([(0, i), (400, i)], fill='#E0E0E0', width=1)
    
    # Grille épaisse
    for i in range(0, 400, 100):
        draw.line([(i, 0), (i, 400)], fill='#B0B0B0', width=2)
        draw.line([(0, i), (400, i)], fill='#B0B0B0', width=2)
    
    return img

def create_blueprint_pattern():
    """Crée un motif type blueprint"""
    img = Image.new('RGB', (400, 400), color='#0D3B66')
    draw = ImageDraw.Draw(img)
    
    # Grille blanche
    for i in range(0, 400, 20):
        draw.line([(i, 0), (i, 400)], fill='#2A6F97', width=1)
        draw.line([(0, i), (400, i)], fill='#2A6F97', width=1)
    
    # Points de référence
    for x in range(0, 400, 100):
        for y in range(0, 400, 100):
            draw.ellipse([x-3, y-3, x+3, y+3], fill='#4A90E2')
    
    return img

def create_circuit_board_pattern():
    """Crée un motif de circuit imprimé"""
    img = Image.new('RGB', (400, 400), color='#1A5F3A')
    draw = ImageDraw.Draw(img)
    
    # Traces du circuit
    import random
    random.seed(42)
    
    for _ in range(30):
        x1, y1 = random.randint(0, 400), random.randint(0, 400)
        x2, y2 = x1 + random.randint(-100, 100), y1 + random.randint(-100, 100)
        draw.line([(x1, y1), (x2, y2)], fill='#FFD700', width=2)
    
    # Points de soudure
    for _ in range(50):
        x, y = random.randint(0, 400), random.randint(0, 400)
        draw.ellipse([x-2, y-2, x+2, y+2], fill='#C0C0C0')
    
    return img

def create_gradient_pattern():
    """Crée un dégradé doux"""
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    for y in range(400):
        # Dégradé du bleu clair au blanc
        r = int(227 + (255-227) * (y/400))
        g = int(242 + (255-242) * (y/400))
        b = 253
        draw.line([(0, y), (400, y)], fill=(r, g, b))
    
    return img

def main():
    """Génère toutes les images d'exemple"""
    output_dir = 'examples/backgrounds'
    os.makedirs(output_dir, exist_ok=True)
    
    print("Génération des images d'exemple...")
    
    # Grille technique
    print("  - Grille technique...")
    grid = create_grid_pattern()
    grid.save(os.path.join(output_dir, 'grid_pattern.png'))
    
    # Blueprint
    print("  - Blueprint...")
    blueprint = create_blueprint_pattern()
    blueprint.save(os.path.join(output_dir, 'blueprint.png'))
    
    # Circuit imprimé
    print("  - Circuit imprimé...")
    circuit = create_circuit_board_pattern()
    circuit.save(os.path.join(output_dir, 'circuit_board.png'))
    
    # Dégradé
    print("  - Dégradé...")
    gradient = create_gradient_pattern()
    gradient.save(os.path.join(output_dir, 'gradient.png'))
    
    print(f"\n✓ 4 images créées dans {output_dir}/")
    print("\nUtilisation:")
    print("  Menu Apparence → Charger image de fond...")
    print(f"  Puis sélectionnez un fichier dans {output_dir}/")

if __name__ == "__main__":
    main()
