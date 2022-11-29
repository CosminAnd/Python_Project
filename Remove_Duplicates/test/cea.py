import os

for root, dir, files in os.walk("D:"):
    for f in files:
        print(os.path.join(root,f))