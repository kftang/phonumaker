import json
import random

if __name__ != '__main__':
    exit()

number_map = {
    '0': ['o'],
    '1': ['i', 'l'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

# # json file
# fd = open('words.json', 'r')
# words = json.loads(fd.read())
# fd.close()

# text file
fd = open('popular.txt', 'r')
words = fd.read().splitlines()
fd.close()

phone_number = input('Enter phone number to make into word: ')

created_phrase = []
created_phrase_len = 0

def find_word(cur_word, phone_number, num_index, max_len):
    # check if current word is a valid word of max length
    if len(cur_word) == max_len and cur_word in words:
        return cur_word
    elif len(cur_word) == max_len or max_len < 1:
        return False

    # list of valid letters given digit we're on
    valid_letters = number_map[phone_number[num_index]]
    random.shuffle(valid_letters)

    # try all valid letters
    for valid_letter in valid_letters:
        # only return results that are valid
        result = find_word(cur_word + valid_letter, phone_number, num_index + 1, max_len)
        if result:
            return result
    return False

fails = 0
while created_phrase_len < len(phone_number):
    # TODO: check f
    if fails > len(phone_number):
        print('Could not find phrase')
        exit()
    word = find_word('', phone_number, created_phrase_len, len(phone_number) - created_phrase_len - fails)
    if word:
        fails = 0
        created_phrase.append(word)
        created_phrase_len += len(word)
        print(word)
    else:
        fails += 1

phrase = ''.join(created_phrase).upper()
final_phrase = []
for i, digit in enumerate(phone_number):
    final_phrase.append(phrase[i])
    if digit == '0':
        final_phrase[i] = '0'
    if digit == '1':
        final_phrase[i] = '1'

final_phrase = ''.join(final_phrase)
print(f'Found a phrase! {final_phrase}')