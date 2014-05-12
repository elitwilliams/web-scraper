from bs4 import BeautifulSoup
import get_html_text

# Returns a concatenated string on all <p> tags from a nytimes.com html file

def get_article_text(webtext):
    article_text = ""
    soup = BeautifulSoup(webtext)
    for tag in soup.findAll('p',attrs={'itemprop':'articleBody'}):
        article_text += tag.contents[0]
    return article_text

# Returns a string of a url's body content

def get_article(url):
    htmltext = get_html_text.get_html_text(url)
    return get_article_text(htmltext)

# Returns dictionary of 25 sorted keywords

def get_keywords(articletext):
    common = open('common.txt').read().split('\n')
    word_dict = {}
    word_list = articletext.lower().split()
    for word in word_list:
        if word not in common and word.isalnum():
            if word not in word_dict:
                word_dict[word] = 1
            if word in word_dict:
                word_dict[word] += 1
    top_words = sorted(word_dict.items(),key=lambda(k,v):(v,k),reverse=True)[0:25]
    top25 = []
    for word in top_words:
        top25.append(word[0])
    return top25  

