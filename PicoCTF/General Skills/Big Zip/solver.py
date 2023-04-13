import os
for root, dirs, files in os.walk('.'):
    for file in files:
        contents = open(os.path.join(root, file), "rb").read().split(b'\n')
        for content in contents:
            if (content.find(b"pico") != -1):
                print(content)
