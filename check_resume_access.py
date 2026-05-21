import cloudinary
import cloudinary.api

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

# Get resource details
try:
    result = cloudinary.api.resource('media/resume/Rahul_Ajagare_Pyhton_1_c7it6n', resource_type='image')
    print('Resource details:')
    print('  access_mode:', result.get('access_mode'))
    print('  url:', result.get('url'))
    print('  secure_url:', result.get('secure_url'))
    print('  Full result keys:', list(result.keys()))
except Exception as e:
    print('Error:', e)

# Also try as image (though it's pdf)
try:
    result2 = cloudinary.api.resource('media/resume/Rahul_Ajagare_Pyhton_1_c7it6n', resource_type='image')
    print('As image:', result2)
except Exception as e:
    print('Error as image:', e)
