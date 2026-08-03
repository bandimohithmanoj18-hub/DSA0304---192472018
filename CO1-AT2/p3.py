import re

text = []

print("Enter Text (Type END on a new line to finish):")

while True:
    line = input()
    if line.strip().upper() == "END":
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

    choice = input("Enter Choice: ").strip()

    if choice == "1":
        result = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
        print(result if result else "No Match Found")

    elif choice == "2":
        result = re.findall(r"\b[6-9]\d{9}\b", text)
        print(result if result else "No Match Found")

    elif choice == "3":
        result = re.findall(r"#\w+", text)
        print(result if result else "No Match Found")

    elif choice == "4":
        result = re.findall(r"@\w+", text)
        print(result if result else "No Match Found")

    elif choice == "5":
        prefix = input("Enter Prefix: ").strip()
        pattern = rf"\b{re.escape(prefix)}\w*\b"
        result = re.findall(pattern, text, re.IGNORECASE)
        print(result if result else "No Match Found")

    elif choice == "6":
        suffix = input("Enter Suffix: ").strip()
        pattern = rf"\b\w*{re.escape(suffix)}\b"
        result = re.findall(pattern, text, re.IGNORECASE)
        print(result if result else "No Match Found")

    elif choice == "7":
        word = input("Enter Word: ").strip()
        pattern = rf"\b{re.escape(word)}\b"
        result = re.findall(pattern, text, re.IGNORECASE)
        print(result if result else "No Match Found")

    elif choice == "8":
        print("Program Terminated")
        break

    else:
        print("Invalid Choice")