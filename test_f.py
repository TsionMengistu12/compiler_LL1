from parser.grammar import parse_grammar
from parser.first_follow import compute_first

grammar_text = """
E -> T E'
E' -> + T E' | ε
T -> F T'
T' -> * F T' | ε
F -> ( E ) | id
"""

grammar, start, _, _ = parse_grammar(grammar_text)
first = compute_first(grammar)

for nt in first:
    print(f"FIRST({nt}) = {first[nt]}")
