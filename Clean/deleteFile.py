import os, os.path

for root, _, files in os.walk("C:/"):
    for f in files:
     #   fullpath = os.path.join(root, f)
      #  if os.path.getsize(fullpath) < 200 * 1024:
       #$ os.remove(fullpath)
        fullpath = os.path.join(root, f)
        if f == '!!!SAVE_FILES_INFO!!!.txt':
            os.remove(fullpath)