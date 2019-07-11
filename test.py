import os
import requests
import subprocess
import hashlib

def md5_hex(text):
    m = hashlib.md5()
    m.update(text.encode('ascii', errors='ignore'))
    return m.hexdigest()

def convert(input_text = "test", size = 300):
	output_file = os.path.join(input_text + '.png')
	if not os.path.exists(output_file):
	    grav_url = "http://www.gravatar.com/avatar/" + \
	    md5_hex(input_text) + "?d=identicon&s=" + str(size)
	    r = requests.get(grav_url)
	    if r.ok:
	        with open(output_file, 'wb') as img:
	            img.write(r.content)
	            print("complete! Here Image URL.")
	            print(grav_url)

if __name__ == '__main__':
	convert(input("Input Your Text: "),
		int(input("Input Size(Only int): ")))