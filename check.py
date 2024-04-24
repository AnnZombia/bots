import os
import time
notify = f'''
osascript -e 'display notification "Page was updated" with title "Warning"'
'''

while True:
    curl = 'wget ya.ru -O check'
    os.system(curl)

    with open('check', 'r+') as file1:
        data = file1.read()
        ha = str (hash(data))
        
    with open('hash', 'r+') as file2:
        last_hash = file2.read()
        if ha == last_hash: pass
        else:   
            file2.truncate(0)
            file2.write(str(ha))
            os.system(notify)
          
    time.sleep(15)
