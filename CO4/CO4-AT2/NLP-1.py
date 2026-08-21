# Question 1

sentence = "Show me the transactions with the card from last month"

print("Sentence:", sentence)

print("\nPossible interpretations:")
print("1. Transactions made using the card")
print("2. Transactions associated with the card")

print("\nCFG Limitation:")
print("CFG cannot easily resolve ambiguity or agreement.")

print("\nPCFG:")
print("Uses probabilities to select the most likely parse.")

print("\nFeature Structure:")
features = {"Number": "Plural", "Verb": "Show"}
print(features)

print("\nImproved Method:")
print("PCFG + Feature Structures + Earley Parsing")

print("\nBenefits:")
print("Better ambiguity handling")
print("Agreement checking")
print("Efficient parsing of long queries")
