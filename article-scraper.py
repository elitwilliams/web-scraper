import article_text
import get_html_text

url = 'http://nyglass.com'

article = article_text.get_article(url)

print article_text.get_keywords(get_html_text.get_html_text(url))
