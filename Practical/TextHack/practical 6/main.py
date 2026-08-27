def sequence_alignment(seq1, seq2):

    m = len(seq1)
    n = len(seq2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = -i

    for j in range(n + 1):
        dp[0][j] = -j

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                score = 1
            else:
                score = -1

            dp[i][j] = max(
                dp[i - 1][j - 1] + score,
                dp[i - 1][j] - 1,
                dp[i][j - 1] - 1
            )

    return dp[m][n]


seq1 = input("Enter Sequence 1: ")
seq2 = input("Enter Sequence 2: ")

score = sequence_alignment(seq1, seq2)

print("Optimal Alignment Score =", score)


values = [10, 20, 30, 40]
max_items = 2

n = len(values)

best_value = 0
best_subset = []

for mask in range(1 << n):

    total = 0
    selected = []

    for i in range(n):

        if mask & (1 << i):
            total += values[i]
            selected.append(values[i])

    if len(selected) <= max_items and total > best_value:
        best_value = total
        best_subset = selected


print("\nBitmask DP")
print("----------")
print("Maximum items =", max_items)
print("Selected items =", best_subset)
print("Maximum value =", best_value)