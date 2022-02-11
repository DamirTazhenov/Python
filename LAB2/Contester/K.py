inp = input()

disallowed_charecter = ",.!?"
for character in disallowed_charecter:
    inp = inp.replace(character,"") #deleting punctuation char

words = list(set(map(str,inp.split())))  #creating a list with unique a words by using set
sorted_words = words.sort()


print (len(words))
for i in words:
    print (i)
