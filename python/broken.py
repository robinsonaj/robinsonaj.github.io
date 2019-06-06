# pages = 457
# word_per_page = 250
# number_of_pieces = 100
#
# each_chunk = (457 * 250)/100
# print(each_chunk)

# text = {
# 	"Jane Eyre": "1847",
# 	"Cane": "1923",
# 	"Wide Sargasso Sea": "1966",
# 	"Citizen: An American Lyrics": "2014"
# }

# for title, date in text.items():
# 	print(title + " was published in " + date + ".")

# words =  ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
# canonical_spellings = ['color','amuck','adviser','pepper']
#
# mappings = {'colour':'color', 'amok':'amuck', 'advisor':'adviser'}
#
# new_list = []
# for word in words:
# 	if word in mappings:
# 		new_list.append(mappings[word])
# 	else:
#             new_list.append(word)
#
# print(new_list)

# domain = 'https://walshbr.gov/'
# pages = ['about','blog','pedagogy', 'projects', 'cv']
#
# urls = []
#
# for thing in pages:
# 	url = (domain + thing)
# 	urls.append(url)
#
# url


authrs = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
    }

for author, date in authrs.items():
    print(author + " died in " + date)
