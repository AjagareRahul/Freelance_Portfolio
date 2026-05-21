import cloudinary
import cloudinary.api

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

# List all uploads
result = cloudinary.api.resources(
    resource_type='image',
    type='upload',
    max_results=50,
    prefix='media/'
)
resources = result.get('resources', [])
print(f'Total Cloudinary images: {len(resources)}')
for r in resources:
    print(f"  public_id: {r['public_id']}")
    print(f"    URL: {r['secure_url']}")
    print(f"    format: {r['format']}, bytes: {r.get('bytes', 'N/A')}")
    print()
