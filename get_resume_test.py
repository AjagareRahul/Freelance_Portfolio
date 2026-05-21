import requests
url = 'https://res.cloudinary.com/dfgp33gvs/image/upload/v1778665312/media/resume/Rahul_Ajagare_Pyhton_1_c7it6n'
r = requests.get(url, timeout=10)
print('GET status:', r.status_code)
print('Content-Type:', r.headers.get('Content-Type'))
print('Content length:', len(r.content))
print('First 100 bytes:', r.content[:100])
