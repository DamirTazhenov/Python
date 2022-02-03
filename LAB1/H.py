word = input()
letter = input()
first = word.find(letter)
last = word.rfind(letter)
if (first==last):
 print(first)
else:
 print(first,last)
