import cloudinary
import cloudinary.api
import requests

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

public_id = 'media/resume/Rahul_Ajagare_Pyhton_1_c7it6n'

# Try fetching as raw
info = cloudinary.api.resource(public_id, resource_type='raw')
print('Access mode (raw):', info.get('access_mode'))
print('Secure URL (raw):', info.get('secure_url'))
url_raw = info.get('secure_url')
r = requests.head(url_raw, timeout=10)
print('HEAD raw URL:', r.status_code)
