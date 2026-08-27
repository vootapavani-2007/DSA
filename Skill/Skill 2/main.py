print("========== ALGORITHMIC PARADIGMS ==========")

print("\n1. Brute Force")
print("2. Divide and Conquer")
print("3. Greedy")
print("4. Dynamic Programming")
print("5. Backtracking")
print("6. Hashing")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    print("\nBrute Force")
    print("Tries all possible solutions.")
    print("Example: Naive Pattern Matching")
    print("Time Complexity: O(n*m)")

elif choice == 2:
    print("\nDivide and Conquer")
    print("Divides a problem into smaller subproblems.")
    print("Example: Merge Sort")
    print("Time Complexity: O(n log n)")

elif choice == 3:
    print("\nGreedy")
    print("Chooses the best option at every step.")
    print("Example: Activity Selection")

elif choice == 4:
    print("\nDynamic Programming")
    print("Stores results of overlapping subproblems.")
    print("Example: Edit Distance")
    print("Time Complexity: O(m*n)")

elif choice == 5:
    print("\nBacktracking")
    print("Builds a solution and backtracks when necessary.")
    print("Example: N-Queens")

elif choice == 6:
    print("\nHashing")
    print("Uses hash values for fast searching.")
    print("Example: Rabin-Karp")

else:
    print("\nInvalid choice!")