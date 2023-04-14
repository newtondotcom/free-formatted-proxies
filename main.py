from urllib.request import urlopen
import os

def download(t_url):
    response = urlopen(t_url)
    data = response.read()
    txt_str = str(data)
    lines = txt_str.split("\\n")
    des_url = 'folder/forcast.csv'
    fx = open(des_url,"w")
    for line in lines:
        fx.write(line+ "\n")
    fx.close()
    return data

#target_url = "https://spys.me/socks.txt" 
#download(target_url)
os.system('wget https://spys.me/socks.txt -O socks.txt')
data = open('socks.txt', 'r').read()
data = data.splitlines(True)
data = data[6:]
print(data)
output = [ ('\"http://' + proxy.split(' ')[0] + '\"\n') for proxy in data ]
correct = open('sources/proxy.txt', 'w').write(''.join(output[:-2]))