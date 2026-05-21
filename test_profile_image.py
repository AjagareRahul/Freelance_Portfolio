import requests
url = 'https://res.cloudinary.com/dfgp33gvs/image/upload/v1/media/profile/rahulimage_hyv5iw.jpg'
r = requests.head(url, timeout=10)
print('Profile image status:', r.status_code)
# Also check get
r2 = requests.get(url, timeout=10)
print('Profile image GET:', r2.status_code, len(r2.content), 'bytes')
