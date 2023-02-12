from collectoins import Counter
from itertolss import chain
last_name = list('Matiash')
words_counter = Counter(chain(*last_name))
print(words_counter)




abc = '3d48fhkldla89dh3'
letters = ''.join([i for i in abc if not i.isdigit()])
print(letters)
