# locate all occurrences of a pattern using kmp strin maching

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    positions = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            positions.append(i - j)  # match found
            j = lps[j - 1]  # continue searching for next match

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]  # skip using LPS
            else:
                i += 1

    return positions