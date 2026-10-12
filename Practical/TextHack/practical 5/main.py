def edit_distance(s1, s2):

    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[m][n]


file = open("words.txt", "r")
words = file.read().splitlines()
file.close()

query = input("Enter search word: ")

print("\nSimilar Words")
print("-------------")

for word in words:

    distance = edit_distance(query.lower(), word.lower())

    if distance <= 3:
        print(word, "Edit Distance =", distance)