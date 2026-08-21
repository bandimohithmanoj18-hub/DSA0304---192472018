# Dialogue Act Classification

dialogue = [
    ("User", "Can you book a train ticket for me?", "Request"),
    ("Agent", "Sure, where would you like to travel?", "Question"),
    ("User", "I want to go to Chennai.", "Inform"),
    ("Agent", "Your ticket has been booked.", "Confirmation")
]

for speaker, text, act in dialogue:
    print(speaker, ":", act)

print("\nDialogue Act Sequence:")
print("Request -> Question -> Inform -> Confirmation")

print("\nPurpose:")
print("These acts help the agent understand the user's intention.")
