import os
from PIL import Image

static_images_dir = r'D:\Freelance_Portfolio\static\images'
os.makedirs(static_images_dir, exist_ok=True)

# Create a simple solid color image for preview
preview = Image.new('RGB', (1200, 630), color='#1a1a2e')
out_path = os.path.join(static_images_dir, 'portfolio-preview.jpg')
try:
    preview.save(out_path, 'JPEG', quality=85)
    print('Saved portfolio-preview.jpg - size:', os.path.getsize(out_path))
except Exception as e:
    print('JPEG save failed:', e)
    # fallback to PNG
    out_path_png = os.path.join(static_images_dir, 'portfolio-preview.jpg')  # still .jpg extension? Better to change template but let's keep.
    # Actually we can't change extension easily; we can still save as JPEG by using different method; but if JPEG fails, maybe we need to reinstall Pillow with JPEG.
    # For now, try saving as PNG and rename .jpg? That would be invalid format.
    # Let's try saving with .png and then see? But template expects .jpg. We could change template to use .png. That's simpler.
    pass
