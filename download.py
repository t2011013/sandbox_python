import time
import urllib.error
import urllib.request
import json
import sys
from bs4 import BeautifulSoup

url = sys.argv[1]
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)

soup = BeautifulSoup(html, "html.parser")

json_list = [img.get('data-preview') for img in soup.find_all(class_='FnStickerPreviewItem')]

url_list = [(json.loads(dat))["staticUrl"] for dat in json_list]

[urllib.request.urlretrieve(url,"{0}".format(str(i) + ".png")) for i, url in enumerate(url_list)]
