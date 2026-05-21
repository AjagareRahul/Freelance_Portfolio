import cloudinary
cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

from cloudinary import CloudinaryResource
# Simulate what storage does
name = 'media/resume/Rahul_Ajagare_Pyhton_1_c7it6n'
res = CloudinaryResource(name, default_resource_type='image')
print('URL from CloudinaryResource:', res.url)
print('Secure URL:', res.secure_url)

# Without leading media
name2 = 'resume/Rahul_Ajagare_Pyhton_1_c7it6n'
res2 = CloudinaryResource(name2, default_resource_type='image')
print('URL without media prefix:', res2.url)

# Check if it adds extension automatically based on format?
# Cloudinary knows the format from asset metadata? But when generating URL without specifying format, it uses default delivery format (maybe the original format).