import cloudinary
cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)
from cloudinary import CloudinaryResource
name = 'media/resume/Rahul_Ajagare_Pyhton_1_c7it6n'
res_image = CloudinaryResource(name, default_resource_type='image')
print('Image URL:', res_image.url)
res_raw = CloudinaryResource(name, default_resource_type='raw')
print('Raw URL:', res_raw.url)
