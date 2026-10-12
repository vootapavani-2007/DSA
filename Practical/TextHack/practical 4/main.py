text = open("sample.txt", "r").read().strip()

pattern = input("Enter pattern: ")

print("\nRabin-Karp Pattern Matching")
print("---------------------------")

m = len(pattern)
pattern_hash = hash(pattern)

for i in range(len(text) - m + 1):
    window = text[i:i + m]

    if hash(window) == pattern_hash:
        if window == pattern:
            print("Pattern found at index", i)


doc1 = open("doc1.txt", "r").read().lower().split()
doc2 = open("doc2.txt", "r").read().lower().split()

common_words = set(doc1).intersection(set(doc2))

print("\nCommon Words:")
print(common_words)

similarity = (
    len(common_words) /
    len(set(doc1).union(set(doc2)))
) * 100

print("Similarity = {:.2f}%".format(similarity))