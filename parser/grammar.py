def parse_grammar(grammar_text):
    grammar = {}
    lines = grammar_text.split("\n")

    start_symbol = None

    for line in lines:
        if "->" not in line:
            continue

    left, right = line.split("->")
    left = left.strip()

    if start_symbol is None:
        start_symbol = left

    productions = []

    for prod in right.split("|"):
        symbols = prod.strip().split()
        productions.append(symbols)

    grammar[left] = productions

    return grammar, start_symbol