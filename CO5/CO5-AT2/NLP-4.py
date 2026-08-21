# Surface Realization

action = "Buy"
agent = "Student"
obj = "Book"
tense = "Past"

if action == "Buy" and tense == "Past":
    sentence = "The student bought a book."

print("Semantic Input:")
print("Action:", action)
print("Agent:", agent)
print("Object:", obj)
print("Tense:", tense)

print("\nGenerated Sentence:")
print(sentence)

print("\nValidation:")
print("Subject + Verb + Object = Correct")
