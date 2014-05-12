import urllib
import re

urls = ['http://www.cnn.com','http://www.nytimes.com','http://youtube.com','http://facebook.com']
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

for url in urls:
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    titles = re.findall(pattern, htmltext) 

    print titles

