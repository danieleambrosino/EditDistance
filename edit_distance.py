import numpy as np


def edit_distance(x, y):
    m = len(x)
    n = len(y)
    c = np.zeros([m + 1, n + 1], dtype=int)

    for i in xrange(m + 1):
        c[i, 0] = i

    for i in xrange(n + 1):
        c[0, i] = i

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            c[i, j] = 1000000

            if x[i - 1] == y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 0

            if x[i - 1] != y[j - 1] and (c[i - 1, j - 1] + 1) < c[i, j]:
                c[i, j] = c[i - 1, j - 1] + 1

            if i >= 2 and j >= 2 and x[i - 1] == y[j - 2] and x[i - 2] == y[
                        j - 1] and (c[i - 2, j - 2] + 2) < c[i, j]:
                c[i, j] = c[i - 2, j - 2] + 2

            if c[i - 1, j] + 1 < c[i, j]:
                c[i, j] = c[i - 1, j] + 1

            if (c[i, j - 1] + 1) < c[i, j]:
                c[i, j] = c[i, j - 1] + 1

    return c[len(x)][len(y)]
