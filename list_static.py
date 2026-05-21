import os
static_dir = r'D:\Freelance_Portfolio\static'
for root, dirs, files in os.walk(static_dir):
    for f in files:
        print(os.path.join(root, f))