# Question 2

machines = ["M1", "M2", "M4"]

print("Active machines:")
for m in machines:
    print("Active(" + m + ") -> Producing(" + m + ")")

print("\nM3:")
print("Maintenance(M3) -> NOT Producing(M3)")

print("\nGear:")
print("Gear production cannot be confirmed.")
print("Produces(M3,Gear) fact is not given.")
