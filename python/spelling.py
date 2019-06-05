words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
canon_word = ['color','amuck','adviser','pepper']


#mappings dictionary
mappings = {'colour':'color', 'amok':'amuck', 'advisor':'adviser'}


#make empty list
new_list = []

#loop over the list of words
for word in words:
    if word in mappings:
        #if a word is misspelled do something
        #correct the spelling using mapping dictionary
        corrected_word = mappings[word]
        #add corrected word
        new_list.append(corrected_word)
    else:
        #if word is correct do something else
        new_list.append(word)



print(new_list)
