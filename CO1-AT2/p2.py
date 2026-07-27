def read_transition_table(states, alphabet):
    transition = {}

    print("\nEnter Transition Table")

    for state in states:
        transition[state] = {}
        for symbol in alphabet:
            nxt = input(f"δ({state}, {symbol}) = ").strip()
            transition[state][symbol] = nxt

    return transition


def simulate_dfa(states, alphabet, transition, start_state, final_states, string):
    current = start_state
    path = [current]

    for ch in string:
        if ch not in alphabet:
            return path, False

        current = transition[current][ch]
        path.append(current)

    return path, current in final_states


def main():
    states = input("Enter states (space separated): ").split()

    alphabet = input("Enter alphabet (space separated): ").split()

    transition = read_transition_table(states, alphabet)

    start_state = input("\nEnter Initial State: ").strip()

    final_states = set(input("Enter Final State(s): ").split())

    t = int(input("\nEnter Number of Test Strings: "))

    for _ in range(t):
        string = input("\nEnter String: ").strip()

        path, accepted = simulate_dfa(
            states,
            alphabet,
            transition,
            start_state,
            final_states,
            string
        )

        print("Transition Path:")
        print(" -> ".join(path))

        if accepted:
            print("Accepted")
        else:
            print("Rejected")


if __name__ == "__main__":
    main()