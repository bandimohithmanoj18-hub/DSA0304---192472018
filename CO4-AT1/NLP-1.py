# Question 1

actual = ["Activate Roaming", "Deactivate Caller Tune",
          "Query Data Balance", "Activate 5G"]

predicted = ["Activate Roaming", "Activate Caller Tune",
             "Query Data Balance", "Activate 5G"]

print("Semantic Representations:")
print("ACTIVATE(Roaming, Customer)")
print("DEACTIVATE(CallerTune, Customer)")
print("QUERY(DataBalance, Customer)")
print("ACTIVATE(5GService, Customer)")

print("\nError:")
for i in range(4):
    if actual[i] != predicted[i]:
        print("Q", i+1, "has an error")

print("Accuracy =", 3/4*100, "%")
