import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://site.hlgs.hlc.edu.tw/bin/home.php'
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'html.parser')

images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_links=sp.find_all(['a', 'img'])
for link in all_links:

    src=link.get('src')
    href = link.get('href') 
    attrs=[src,href]
    for attr in attrs:
        if attr != None and ('.jpeg' in attr or '.png' in attr):
            full_path = attr
            filename = full_path.split('/')[-1]
            print(full_path)
    
            try:
                image = urlopen(full_path)
                f= open(os.path.join(images_dir,filename), 'wb')
                f.write(image.read())
                f.close()
            except:
                print("{}無法讀取!".format(filename))
