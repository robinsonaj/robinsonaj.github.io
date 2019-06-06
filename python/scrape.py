# get libraries
import nltk
from bs4 import BeautifulSoup
from urllib import request

# store the url we're using
url = "https://github.com/humanitiesprogramming/scraping-corpus"

# using that url, get the HTML
html = request.urlopen(url).read()

# turning the URL and turned it into a soup object
soup = BeautifulSoup(html, 'lxml')
our_text = soup.text
links = soup.find_all('a')[1:10]

#print(our_text[0:2000])
# reduce white space (\n = "new line")
#print(soup.text.replace('\n', ' '))

# grab link html on page
links_html = soup.select('td.content a')
# grab specific link html
this_link = links_html[0]
# grab the file path
#print(this_link['href'])

urls = []
# tidy up the code for importing
for link in links_html:
    to_append = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + to_append)

#test_url = urls[3]
corpus_texts = []

for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
    print("Scraping " + url)

print(len(corpus_texts))
print(len(corpus_texts[0]))

this_text = corpus_texts[0]
process_this_text = nltk.word_tokenize(this_text)
print(process_this_text[0:20])
print(nltk.FreqDist(process_this_text).most_common(50))
