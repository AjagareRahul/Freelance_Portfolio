import subprocess
result = subprocess.run(['python', '-c', 'import cloudinary_storage; print(cloudinary_storage.__file__)'], capture_output=True, text=True)
print('cloudinary_storage imported:', result.stdout)
print('stderr:', result.stderr)

# Also try MediaCloudinaryStorage
result2 = subprocess.run(['python', '-c', 'from cloudinary_storage.storage import MediaCloudinaryStorage; print(MediaCloudinaryStorage.__module__)'], capture_output=True, text=True)
print('MediaCloudinaryStorage module:', result2.stdout)
print('stderr:', result2.stderr)
