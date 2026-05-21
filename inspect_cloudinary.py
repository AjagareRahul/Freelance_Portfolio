import cloudinary_storage
import inspect
print(inspect.getfile(cloudinary_storage))

# Show source of the storage module
import cloudinary_storage.storage as cs
print('\n=== storage.py source ===')
print(inspect.getsource(cs))
