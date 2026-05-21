import requests
url = 'https://res.cloudinary.com/dfgp33gvs/raw/upload/v1/media/resume/Rahul_Ajagare_Pyhton_1_c7it6n'
r = requests.head(url, timeout=10)
print('HEAD status:', r.status_code)
r2 = requests.get(url, timeout=10)
print('GET status:', r2.status_code, 'len', len(r2.content))