import requests
base = 'https://res.cloudinary.com/dfgp33gvs/image/upload/v1778665312/media/resume/Rahul_Ajagare_Pyhton_1_c7it6n'
urls = [
    base,
    base + '.pdf',
    base + '?dl=1',
    base + '.pdf?dl=1',
]
for u in urls:
    try:
        r = requests.head(u, timeout=10)
        print(f'{u} -> {r.status_code}')
    except Exception as e:
        print(f'{u} -> Error: {e}')
