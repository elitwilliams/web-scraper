from bs4 import BeautifulSoup
import get_html_text

def get_article_text(webtext):
    article_text = ""
    soup = BeautifulSoup(webtext)
    for tag in soup.findAll('p',attrs={'itemprop':'articleBody'}):
        article_text += tag.contents[0]
    return article_text

def get_article(url):
    htmltext = get_html_text.get_html_text(url)
    return get_article_text(htmltext)
