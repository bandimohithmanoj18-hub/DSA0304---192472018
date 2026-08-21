import re

def parse(expression):
    pattern = r"(forall|exists)\s+([a-z])\s*\((\w+)\((\w+)\)\)"
    
    if re.fullmatch(pattern, expression):
        print("Valid FOPC expression")
    else:
        print("Invalid FOPC expression")

parse("forall x (Human(x))")
