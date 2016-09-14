import random


def mimic_dict(text):
    """Returns mimic dict mapping each word to list of words which follow it."""
    text_list = text.split()
    text_dict = {}

    anterior = ''
    for key in text_list:

        if anterior not in text_dict:
            text_dict[anterior] = []
            text_dict[anterior].append(key)
        else:
            text_dict[anterior].append(key)

        anterior = key

    if key not in text_dict:
        text_dict[key] = ''
    else:
        text_dict[key].append('')

    return text_dict


def mimic(t_dict, word):
    """Given mimic dict and start word, prints 200 random words."""

    frase = ''
    count = 0

    for i in range(200):
        if t_dict[word]:
            random_word = random.choice(t_dict[word])
        else:
            random_word = ''

        if count < 70:
            frase += random_word + ' '
        else:
            frase += "\n"
            count = 0

        count += len(word)
        word = random_word

    return frase
