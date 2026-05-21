import cloudinary
import cloudinary.api

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

# Fetch ALL resources (no prefix filter)
result = cloudinary.api.resources(
    resource_type='image',
    type='upload',
    max_results=100
)
resources = result.get('resources', [])
print(f'Total images in Cloudinary: {len(resources)}')
for r in resources:
    print(f"  public_id: {r['public_id']}")
    print(f"    secure_url: {r['secure_url']}")
    print()
