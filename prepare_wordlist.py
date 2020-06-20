import json
from collections import defaultdict

fd = open('popular.txt', 'r')
words = fd.read().splitlines()
fd.close()

prepared_words = defaultdict(list)

for word in words:
    first_char = word[0]
    prepared_words[first_char].append(word)

fd = open('words.json', 'w')
fd.write(json.dumps(prepared_words, indent=2))
fd.close()