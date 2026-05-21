import os
from PIL import Image, ImageDraw

static_images_dir = r'D:\Freelance_Portfolio\static\images'
os.makedirs(static_images_dir, exist_ok=True)

preview = Image.new('RGB', (1200, 630), color='#1a1a2e')
draw = ImageDraw.Draw(preview)
draw.text((50, 250), "Ajagare Rahul - Python & Django Developer", fill='#ffc107')
out_path = os.path.join(static_images_dir, 'portfolio-preview.jpg')
print('Saving to', out_path)
try:
    preview.save(out_path, 'JPEG', quality=85)
    print('Saved successfully')
except Exception as e:
    print('Error saving:', e)
