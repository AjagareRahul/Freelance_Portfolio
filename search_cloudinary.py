import cloudinary
import cloudinary.api

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

# Search for any resource containing 'rawmaterail' or 'midnight' etc.
keywords = ['rawmaterail', 'midnight', 'cheers']
for kw in keywords:
    result = cloudinary.api.resources(
        resource_type='image',
        type='upload',
        max_results=10,
        prefix=kw
    )
    resources = result.get('resources', [])
    if resources:
        print(f'Found with {kw}:')
        for r in resources:
            print(f"  {r['public_id']}")
    else:
        print(f'No resources with {kw}')

# Also list ALL with folder 'projects' or 'gallery' or 'upcoming'
for folder in ['projects', 'gallery', 'upcoming_projects']:
    result = cloudinary.api.resources(
        resource_type='image',
        type='upload',
        max_results=50,
        prefix=folder
    )
    resources = result.get('resources', [])
    if resources:
        print(f'\nFolder {folder} ({len(resources)}):')
        for r in resources:
            print(f"  {r['public_id']}")
    else:
        print(f'\nNo resources in folder {folder}')
