import mechanize

def get_html_text(url):
    br = mechanize.Browser()
    htmltext = br.open(url).read()
    return htmltext

def get_html_file(url):
    br = mechanize.Browser()
    htmlfile = br.open(url)
    return htmlfile
