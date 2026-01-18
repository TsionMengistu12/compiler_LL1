## we must compute the first of the grammar 

def compute_first(grammar):
    first = {nt: set() for nt in grammar}

    def first_of(symbol):
        if symbol not in grammar:
            return {symbol}
        return first[symbol]
    
    changed = True

    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                i = 0
                while True:
                    before = len(first[nt])
                    f = first_of(production[i])
                    first[nt].update(f - {"ε"})

                    if "ε" not in f:
                        break

                    i += 1
                    if i == len(production):
                        first[nt].add("ε")
                        break

                    if len(first[nt]) > before:
                        changed = True
    return first


def compute_follow(grammar, first, start_symbol):
    follow = {nt: set() for nt in grammar}
    follow[start_symbol].add("$")

    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        before = len(follow[symbol])

                        if i + 1 < len(production):
                            next_sym = production[i + 1]
                            if next_sym in grammar:
                                follow[symbol].update(first[next_sym] - {"ε"})
                                if "ε" in first[next_sym]:
                                    follow[symbol].update(follow[nt])
                            else:
                                follow[symbol].add(next_sym)
                        else:
                            follow[symbol].update(follow[nt])

                        if len(follow[symbol]) > before:
                            changed = True

    return follow

        