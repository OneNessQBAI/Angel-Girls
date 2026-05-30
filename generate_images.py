from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(name, filename, color, width=400, height=500):
    img = Image.new('RGB', (width, height), color=color)
    draw = ImageDraw.Draw(img)
    
    # Draw a simple silhouette/avatar shape
    # Head
    draw.ellipse([150, 80, 250, 200], fill='white', outline='black', width=2)
    # Body
    draw.polygon([(150, 200), (250, 200), (280, 400), (120, 400)], fill='white', outline='black', width=2)
    # Hair
    draw.arc([145, 75, 255, 205], 0, 360, fill='black', width=4)
    
    # Add name text
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Center the text
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    draw.text((text_x, 420), name, fill='white', font=font)
    
    img.save(filename)
    print(f"Created {filename}")

# Create profile images with different colors
profiles = [
    ("Sofia", "assets/sofia.jpg", (180, 40, 80)),
    ("Isabella", "assets/isabella.jpg", (40, 80, 160)),
    ("Valentina", "assets/valentina.jpg", (160, 60, 120)),
    ("Camila", "assets/camila.jpg", (60, 140, 80)),
    ("Luna", "assets/luna.jpg", (200, 140, 40)),
    ("Gabriela", "assets/gabriela.jpg", (80, 40, 140)),
    ("Angelina", "assets/angelina.jpg", (180, 100, 60)),
    ("Victoria", "assets/victoria.jpg", (40, 120, 140)),
]

for name, filename, color in profiles:
    create_placeholder_image(name, filename, color)

print("All placeholder images created!")
