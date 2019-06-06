domain = 'http://walshbr.com/'
pages = ['index', 'about', 'blog', 'pedagogy', 'projects', 'cv']
urls = []

for page in pages:
    urls.append(domain+page)

#comprehension style
# urls = [domain + page for page in pages]

print(urls)
