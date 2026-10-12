file = open("articles.txt", "r")

articles = file.readlines()

file.close()

query = input("Enter keyword: ")

print("\nMatching Articles:")
print("------------------")

found = False

for article in articles:

    if query.lower() in article.lower():
        print(article.strip())
        found = True

if not found:
    print("No matching article found.")