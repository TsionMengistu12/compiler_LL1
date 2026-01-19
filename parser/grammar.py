def parse_grammar(grammar_text):
    grammar = {}
    non_terminals = set()
    terminals = set()

    lines = grammar_text.split("\n")
    start_symbol = None

    for line_no , line in enumerate(lines, start=1):

        line = line.strip()
        if not line:
            continue
    
        if "->" not in line:
            raise ValueError(f"Invalid grammar at line {line_no}: missing '->' ")

        left, right = line.split("->")
        left = left.strip()

        if not left[0].isupper():
            raise ValueError(f"Invalid non-terminal {left} at line {line_no}")

        if start_symbol is None:
            start_symbol = left

        productions = []

        for prod in right.split("|"):
            symbols = prod.strip().split()
            if not symbols:
                raise ValueError(f"Empty production at line {line_no}")
            productions.append(symbols)

        grammar[left] = productions

    # Identify terminals
    for nt in grammar:
        for production in grammar[nt]:
            for symbol in production:
                if symbol not in grammar and symbol != "ε":
                    terminals.add(symbol)
    terminals.add("$")

    return grammar, start_symbol, non_terminals, terminals