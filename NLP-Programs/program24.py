def dialog_act(sentence):
    s = sentence.lower()

    if "?" in sentence:
        return "Question"
    elif s.startswith(("please", "could", "can you")):
        return "Request"
    elif s in ["yes", "okay", "sure"]:
        return "Agreement"
    else:
        return "Statement"

text = "Can you help me?"

print(dialog_act(text))
