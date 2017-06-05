import edit_distance
import divide


def test_edit(query, distance):
    with open('res/names.txt') as names:
        result = []
        for i in names:
            name = i[:len(i) - 1]
            m = edit_distance.edit_distance(query, name)
            if m <= int(distance):
                result.append(name)
        return result


def test_ngram(query, distance, n):
    assert n == 2 or n == 3
    ngram_query = []
    # Divide name in ngrams
    if n == 2:
        ngram_query = divide.digram(query)
    if n == 3:
        ngram_query = divide.trigram(query)

    result = []
    for gram in ngram_query:
        if n == 2:
            words = open('res/digrams/' + gram + '-gram.txt')
        else:
            words = open('res/trigrams/' + gram + '-gram.txt')

        for w in words:
            name = w[:len(w) - 1]
            edit_distance_result = edit_distance.edit_distance(query, name)
            if edit_distance_result <= int(distance):
                if name not in result:
                    result.append(name)
        words.close()
    return result
