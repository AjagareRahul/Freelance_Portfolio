import subprocess
result = subprocess.run(
    ['git', 'log', '--all', '--full-history', '--pretty=oneline', '--', 'media/projects', 'media/gallery', 'media/upcoming_projects'],
    capture_output=True, text=True, cwd=r'D:\Freelance_Portfolio'
)
print('Git log for image paths:')
print(result.stdout[:2000])

# Also check if any image files are tracked
result2 = subprocess.run(
    ['git', 'ls-files', '--', 'media/*', 'static/images/*'],
    capture_output=True, text=True, cwd=r'D:\Freelance_Portfolio'
)
print('Tracked media/static/image files:')
print(result2.stdout)
