def finite_state_automaton(string):
    state = 0

    for ch in string:

        if ch not in ('a', 'b'):
            return False

        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 1
            else:
                state = 2

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2


string = input("Enter a string: ").strip()

if finite_state_automaton(string):
    print("Accepted")
else:
    print("Rejected")