import os
static_images_dir = r'D:\Freelance_Portfolio\static\images'
os.makedirs(static_images_dir, exist_ok=True)

from PIL import Image, ImageDraw

# Create a simple favicon (32x32) with a colored background and maybe letter
favicon = Image.new('RGB', (32, 32), color='#ffc107')
d = ImageDraw.Draw(favicon)
d.text((8, 8), "R", fill='#1a1a2e')
favicon.save(os.path.join(static_images_dir, 'favicon.png'), 'PNG')

# Create a portfolio preview image (1200x630) with gradient-like background
preview = Image.new('RGB', (1200, 630), color='#1a1a2e')
draw = ImageDraw.Draw(preview)
# Add some text
draw.text((50, 250), "Ajagare Rahul - Python & Django Developer", fill='#ffc107')
preview.save(os.path.join(static_images_dir, 'portfolio-preview.jpg'), 'JPEG', quality=85)

print('Images created.')
