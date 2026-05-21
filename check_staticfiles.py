import os
staticfiles_path = r'D:\Freelance_Portfolio\staticfiles'
if os.path.exists(staticfiles_path):
    files = os.listdir(staticfiles_path)
    print('staticfiles dir contents:', files[:10])
else:
    print('staticfiles dir does not exist')
# Also check for manifest file
manifest_path = os.path.join(staticfiles_path, 'staticfiles.json')
print('manifest exists:', os.path.exists(manifest_path))
