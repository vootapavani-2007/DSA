def compute_lps(pattern):

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

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


def naive_search(text, pattern):

    positions = []

    for i in range(len(text) - len(pattern) + 1):

        if text[i:i + len(pattern)] == pattern:
            positions.append(i)

    return positions


def kmp_search(text, pattern):

    lps = compute_lps(pattern)

    positions = []

    i = 0
    j = 0

    while i < len(text):

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):

            positions.append(i - j)
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


text = input("Enter text: ")
pattern = input("Enter pattern: ")

print("\n========== NAIVE PATTERN MATCHING ==========")

naive_result = naive_search(text, pattern)

print("Pattern positions:", naive_result)

print("\n========== KMP PATTERN MATCHING ==========")

kmp_result = kmp_search(text, pattern)

print("Pattern positions:", kmp_result)

print("\n========== LPS ARRAY ==========")

print(compute_lps(pattern))