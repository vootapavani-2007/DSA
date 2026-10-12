print("========== ALGORITHM EVALUATION ==========")

algorithms = {
    1: ("Naive Pattern Matching", "O(n*m)", "Simple, but slow for large text"),
    2: ("KMP", "O(n+m)", "Efficient pattern matching"),
    3: ("Rabin-Karp", "Average O(n+m)", "Uses hashing"),
    4: ("Edit Distance", "O(m*n)", "Useful for fuzzy search"),
    5: ("Binary Search", "O(log n)", "Requires sorted data")
}

print("\nAvailable Algorithms:")

for key, value in algorithms.items():
    print(key, ".", value[0])

choice = int(input("\nSelect an algorithm: "))

if choice in algorithms:

    name, complexity, description = algorithms[choice]

    print("\n========== SELECTED ALGORITHM ==========")
    print("Algorithm:", name)
    print("Time Complexity:", complexity)
    print("Description:", description)

    if choice == 1:
        print("Best for: Small text and simple searching")

    elif choice == 2:
        print("Best for: Large text and repeated pattern searching")

    elif choice == 3:
        print("Best for: Multiple pattern searches")

    elif choice == 4:
        print("Best for: Spelling correction and fuzzy search")

    elif choice == 5:
        print("Best for: Searching sorted data")

else:
    print("Invalid choice!")