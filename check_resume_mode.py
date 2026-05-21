import cloudinary
import cloudinary.api
import json

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

result = cloudinary.api.resource('media/resume/Rahul_Ajagare_Pyhton_1_c7it6n', resource_type='image')
print('access_mode:', result.get('access_mode'))
# Also get the raw JSON
print('Full JSON (truncated):', json.dumps(result, indent=2)[:1000])
