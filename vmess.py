import requests
import os

url = 'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt'
response = requests.get(url)
f1 = response.content
open('all.txt', 'w').write(f1.decode('ascii'))
del f1

f1 = open('all.txt', 'r')
f2 = open('vmess.txt', 'w')
f3 = open('ss.txt', 'w')

line = f1.readline()
while line:
    if line[0:5] == 'vmess':
        f2.write(line)
    elif line[0:2] == 'ss':
        f3.write(line)
    line = f1.readline()

f1.close()
f2.close()
f3.close()

os.system('cp ./all.txt ./storage/downloads/vmess/')
os.system('cp ./vmess.txt ./storage/downloads/vmess/')
os.system('cp ./ss.txt ./storage/downloads/vmess/')


print('finished')