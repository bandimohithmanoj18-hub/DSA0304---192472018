# Question 3

sentence = ("The doctor who reviewed the patient last week "
            "recommends starting medication and scheduling "
            "a follow-up visit in Chennai.")

print("Input:")
print(sentence)

print("\n1. CFG:")
print("Identifies sentence structure.")

print("\n2. PCFG:")
print("Selects the most probable interpretation.")

print("\n3. Feature Structure:")
features = {
    "Subject": "Doctor",
    "Number": "Singular",
    "Verb": "recommends"
}
print(features)

print("\n4. Sub-categorization:")
print("recommends -> medication")
print("recommends -> follow-up visit")

print("\n5. Structured Output:")
print("Diagnosis : Not specified")
print("Action    : Start medication")
print("Action    : Schedule follow-up")
print("Location  : Chennai")

print("\n6. Hospital Improvements:")
print("Use Earley parsing")
print("Use medical dictionaries")
print("Use PCFG probabilities")
print("Use real-time processing")
print("Use scalable NLP models")
