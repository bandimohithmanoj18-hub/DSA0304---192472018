# Question 2

sentence = "Book a flight to Delhi with a window seat"

print("Sentence:", sentence)

print("\nPossible meanings:")
print("1. Book a flight to Delhi + window seat")
print("2. Flight to Delhi with a specific seat preference")

print("\nTop-Down Parsing:")
print("Starts from the grammar start symbol.")
print("May require backtracking.")
print("Slow for ambiguous input.")

print("\nEarley Parsing:")
print("Handles ambiguous sentences.")
print("Handles incomplete input.")
print("Uses dynamic programming.")

print("\nComparison:")
print("Top-Down -> More backtracking")
print("Earley   -> More efficient for ambiguous input")
