import os
from PIL import Image

static_images_dir = r'D:\Freelance_Portfolio\static\images'
os.makedirs(static_images_dir, exist_ok=True)

# Create a simple solid color image for preview
preview = Image.new('RGB', (1200, 630), color='#1a1a2e')
out_path = os.path.join(static_images_dir, 'portfolio-preview.png')
preview.save(out_path, 'PNG')
print('Saved portfolio-preview.png, size:', os.path.getsize(out_path))
