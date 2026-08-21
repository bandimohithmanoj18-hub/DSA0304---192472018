# Question 4

roles = {
    "Doctor": "Agent",
    "Patient": "Recipient",
    "Headache": "Symptom",
    "Medicine": "Object/Theme"
}

print("Semantic Roles:")
for word, role in roles.items():
    print(word, "->", role)

print("\nSyntax: Subject-Verb-Object")
print("Dependency parsing improves accuracy.")
