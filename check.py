import os
import time
import hashlib

while True:
    curl = 'wget ya.ru -O check'
    os.system(curl)
    with open(check, 'rb') as f:
        hash = hashlib.file_digest(f, 'sha256').hexdigest()
        print('new hash:', hash)
        
    with open("file","w+") as f:
        last_hash = f.readline()
        print('previous hash:', last_hash)
        if hash == last_hash: pass
        else:   
            f.truncate(0)
            f.write(hash)
          
    time.sleep(60)

  
