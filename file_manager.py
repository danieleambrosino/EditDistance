import divide
import string


def ngram_populate():
    # generate digram files
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            open('res/digrams/' + i + j + '-gram.txt', 'w').close()

    # generate trigram files
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                open('res/trigrams/' + i + j + k + '-gram.txt', 'w').close()

    # divide first names in n-grams
    with open('res/names.txt') as names:
        for k in names:
            name = k[:len(k) - 1]
            gram = divide.digram(name)
            for z in gram:
                file_name = 'res/digrams/' + z + '-gram.txt'
                with open(file_name, 'a') as f:
                    f.write(name + '\n')

        names.seek(0)
        for k in names:
            name = k[:len(k) - 1]
            gram = divide.trigram(name)
            for z in gram:
                file_name = 'res/trigrams/' + z + '-gram.txt'
                with open(file_name, 'a') as f:
                    f.write(name + '\n')
