import re


text = []

print("Enter Text (type END to stop):")

while True:
    line = input()
    if line.upper() == "END":
        break
    text.append(line)

text = "\n".join(text)


while True:

    print("\n========== MENU ==========")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)

        print("\nDates Found:")
        print(result if result else "No Match Found")

    elif choice == "2":

        result = re.findall(r'\b[6-9]\d{9}\b', text)

        print("\nPhone Numbers Found:")
        print(result if result else "No Match Found")

    elif choice == "3":

        result = re.findall(r'#\w+', text)

        print("\nHashtags Found:")
        print(result if result else "No Match Found")

    elif choice == "4":

        result = re.findall(r'@\w+', text)

        print("\nMentions Found:")
        print(result if result else "No Match Found")

    elif choice == "5":

        prefix = input("Enter Prefix: ")

        pattern = r'\b' + re.escape(prefix) + r'\w*\b'

        result = re.findall(pattern, text, flags=re.IGNORECASE)

        print("\nWords Found:")
        print(result if result else "No Match Found")

    elif choice == "6":

        suffix = input("Enter Suffix: ")

        pattern = r'\b\w*' + re.escape(suffix) + r'\b'

        result = re.findall(pattern, text, flags=re.IGNORECASE)

        print("\nWords Found:")
        print(result if result else "No Match Found")

    elif choice == "7":

        word = input("Enter Word: ")

        pattern = r'\b' + re.escape(word) + r'\b'

        result = re.findall(pattern, text, flags=re.IGNORECASE)

        print("\nWords Found:")
        print(result if result else "No Match Found")

    elif choice == "8":

        print("Program Terminated")
        break

    else:
        print("Invalid Choice")