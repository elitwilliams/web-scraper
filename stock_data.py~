import urllib
import re

symbolfile = open('symbols.txt')
symbolslist = symbolfile.read()  

newsymbolslist = symbolslist.split('\n')

symbolslist = ['aapl','spy','amzn','goog','nflx']

for symbol in newsymbolslist:
    url = 'http://finance.yahoo.com/q?s='+symbol+'&ql=1'
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print symbol.upper(),': ',price[0]
