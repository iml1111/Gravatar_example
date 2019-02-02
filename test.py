import os
import requests
import subprocess
import hashlib

size = 300
# Write here
input_text = "iml1111"
file_name = input_text

def md5_hex(text):
    m = hashlib.md5()
    m.update(text.encode('ascii', errors='ignore'))
    return m.hexdigest()

output_file = os.path.join(file_name + '.png')
if not os.path.exists(output_file):
    grav_url = "http://www.gravatar.com/avatar/" + md5_hex(input_text) + "?d=identicon&s=" + str(size)
    r = requests.get(grav_url)
    if r.ok:
        with open(output_file, 'wb') as img:
            img.write(r.content)
            print(grav_url)