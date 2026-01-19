## we must compute the first of the grammar 

def compute_first(grammar):
    first = {nt: set() for nt in grammar}

    def is_terminal(symbol):
        return symbol not in grammar and symbol != "ε"

    changed = True
    while changed:
        changed = False

        for nt in grammar:
            for production in grammar[nt]:
                add_epsilon = True

                for symbol in production:
                    before = len(first[nt])

                    # Terminal
                    if is_terminal(symbol):
                        first[nt].add(symbol)
                        add_epsilon = False

                    # Epsilon
                    elif symbol == "ε":
                        # epsilon production
                        first[nt].add("ε")
                        add_epsilon = False

                    # Non-terminal
                    else:
                        first[nt].update(first[symbol] - {"ε"})
                        if "ε" not in first[symbol]:
                            add_epsilon = False


                    if len(first[nt]) > before:
                        changed = True

                    if not add_epsilon:
                        break

                if add_epsilon:
                    if "ε" not in first[nt]:
                        first[nt].add("ε")
                        changed = True

    return first


def compute_follow(grammar, first, start_symbol):
    follow = {nt: set() for nt in grammar}
    follow[start_symbol].add("$")

    changed = True
    while changed:
        changed = False

        for A in grammar:
            for production in grammar[A]:
                for i, B in enumerate(production):
                    if B not in grammar:
                        continue

                    before = len(follow[B])

                    # β = production[i+1:]
                    beta = production[i + 1:]

                    if beta:
                        add_follow_A = True

                        for symbol in beta:
                            if symbol in grammar:
                                follow[B].update(first[symbol] - {"ε"})
                                if "ε" in first[symbol]:
                                    continue
                                add_follow_A = False
                                break
                            else:
                                follow[B].add(symbol)
                                add_follow_A = False
                                break

                        if add_follow_A:
                            follow[B].update(follow[A])
                    else:
                        follow[B].update(follow[A])

                    if len(follow[B]) > before:
                        changed = True

    return follow
