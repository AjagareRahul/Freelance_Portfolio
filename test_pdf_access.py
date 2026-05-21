import requests
url = 'https://res.cloudinary.com/dfgp33gvs/image/upload/v1778665312/media/resume/Rahul_Ajagare_Pyhton_1_c7it6n.pdf'
try:
    r = requests.get(url, timeout=10)
    print('GET', url)
    print('Status:', r.status_code)
    print('Content-Type:', r.headers.get('Content-Type'))
    print('Content length:', len(r.content))
except Exception as e:
    print('Error:', e)
