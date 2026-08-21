# Q4: Entropy

import math

p_is = 0.66
p_drives = 0.33

entropy = -(p_is * math.log2(p_is) +
            p_drives * math.log2(p_drives))

print("QUESTION 4")
print("--------------------")
print("P(is) =", p_is)
print("P(drives) =", p_drives)
print("Entropy =", round(entropy, 3), "bits")
