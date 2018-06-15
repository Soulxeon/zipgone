import os
import time
#seleccionar path
path = "Path/directory"
test = os.listdir(path)
current_time = time.time()
for item in test:
    creation_time = os.path.getctime(path+"/"+item)
    if item.endswith(".zip") and (current_time - creation_time) // (24 * 3600) >= 1:
        os.remove(os.path.join(path, item))
