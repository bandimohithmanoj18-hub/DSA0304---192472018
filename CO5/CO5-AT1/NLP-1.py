# Q1 Coreference Resolution

text = "John and Mary went to the park. He brought a ball. She played with it. The dog chased him. They went home."

print("MENTIONS AND RESOLUTION")
print("He  -> John")
print("She -> Mary")
print("it  -> ball")
print("him -> John")
print("They -> John, Mary and dog")

print("\nRESOLVED PARAGRAPH")
print("John brought a ball.")
print("Mary played with the ball.")
print("The dog chased John.")
print("John, Mary and the dog went home.")
