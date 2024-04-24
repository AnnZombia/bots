import os
import time

while True:
    curl = 'wget ya.ru -O check' 
    hash = hash(curl)
    last_hash = f.readline()

    with open("file","w+") as f:
        last_hash = f.readline()
        if hash == last_hash: pass
        else:   
            f.truncate(0)
            f.write(hash)
          
    time.sleep(60)

  
