import threading
import re
import requests
from Queue import Queue,Empty
from bs4 import BeautifulSoup

NUM_THREADS = 10
TIMEOUT = 10
BASE_URL = 'http://www.nyglass.com'
p = re.compile('[^A-Za-z0-9]+')
BLACKLIST = set(['the', 'and', 'a', 'it'])
lock = threading.Lock()

class CrawlingThread(threading.Thread):
    def __init__(self, todo, visited, index):
         threading.Thread.__init__(self)
         self.todo = todo
         self.visited = visited
         self.products = set()
         self.index = index

    def indexText(self, text, url):
        tokens = p.split(text)
        to_index = set(tokens) - BLACKLIST
        for token in to_index:
            if token not in self.index:
                try:
                    lock.acquire()
                    self.index[token] = set()
                finally:
                    lock.release()
            self.index[token].add(url)

    def run(self):
        while not self.todo.empty():
            try:
                url = self.todo.get(True, TIMEOUT)
                if url in self.visited:
                    continue
                r = requests.get(url)
                if r.status_code == 200:
                    data = r.text
                    soup = BeautifulSoup(data)
                    for link in soup.find_all('a'):
                        href = link.get('href')
                        if href.startswith('/'):
                            new_url = BASE_URL + href
                            if not new_url in self.visited:
                                self.todo.put(new_url)
                    if '/product' in url:
                        links = soup.findAll('link', rel='canonical')
                        url_to_index = url
                        for link in links:
                            self.products.add(link.get('href'))
                            print link.get('href')
                            url_to_index = link.get('href')
                        description = soup.findAll('div', {'class':'description'})
                        for div in description:
                            text = ' '.join([p.getText() for p in div.findAll('p')]).lower()
                            self.indexText(text, url_to_index)
                self.visited.add(url)
            except (Empty, KeyboardInterrupt, SystemExit):
                break

if __name__ == '__main__':
    index = {}
    todo = Queue()
    todo.put(BASE_URL)
    visited_urls = set()
    threads = []
    for i in range(NUM_THREADS):
        t = CrawlingThread(todo, visited_urls, index)
        t.daemon = True
        threads.append(t)
    for t in threads:
        t.start()
    total_products = 0
    for t in threads:
        t.join()
        total_products += len(t.products)
    print "Total products found => %s" % total_products
    try:
        while True:
            s = raw_input('enter search terms: ')
            terms = s.lower().split()
            for term in terms:
                term_sets = []
                if term in index:
                    term_sets.append(set(index[term]))
                if len(term_sets) > 0:
                    results = term_sets[0]
                    for i in range(1, len(term_sets)):
                        results = results.intersection(term_sets[i])
                    for result in results:
                        print result
    except EOFError:
        print 'Goodbye!'

