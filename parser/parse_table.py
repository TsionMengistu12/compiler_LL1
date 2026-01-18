def build_parse_table(grammar, first, follow):
    table = {nt: {} for nt in grammar}

    for nt in grammar:
        for production in grammar[nt]:

            prod_first = set()
            for symbol in production:
                if symbol in grammar:
                    prod_first.update(first[symbol] - {"ε"})
                    if "ε" not in first[symbol]:
                        break
                else:
                    prod_first.add(symbol)
                    break
            else:
                prod_first.add("ε")

            for terminal in prod_first:
                if terminal != "ε":
                    table[nt][terminal] = production

            if "ε" in prod_first:
                for terminal in follow[nt]:
                    table[nt][terminal] = ["ε"]

    return table
