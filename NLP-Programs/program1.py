import re

text = input("Enter the text:\n")
pattern = input("Enter the regular expression: ")

try:
    match = re.match(pattern, text, re.IGNORECASE)
    search = re.search(pattern, text, re.IGNORECASE)
    findall = re.findall(pattern, text, re.IGNORECASE)

    print("\n----- RESULTS -----")

    if match:
        print("Match      :", match.group())
    else:
        print("Match      : No Match Found")

    if search:
        print("Search     :", search.group())
    else:
        print("Search     : Pattern Not Found")

    if findall:
        print("Find All   :", findall)
        print("Occurrences:", len(findall))
    else:
        print("Find All   : No Occurrences")

    replacement = input("\nEnter replacement word: ")

    modified = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    print("\nModified Text:")
    print(modified)

except re.error:
    print("Invalid Regular Expression")