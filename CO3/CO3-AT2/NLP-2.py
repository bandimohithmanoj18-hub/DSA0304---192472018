# Q2: Backoff Model

p_science_data = 3 / 3

# "science improves" is unseen
p_improves_science = 0

# "improves" is also unseen
p_improves = 0

final_probability = p_science_data * p_improves_science

print("QUESTION 2")
print("--------------------")
print("P(science | data) =", p_science_data)
print("P(improves | science) =", p_improves_science)
print("P(improves) =", p_improves)
print("Backoff Probability =", final_probability)
