from parser.grammar import parse_grammar
from parser.first_follow import compute_first, compute_follow
from parser.parse_table import build_parse_table

def run_ll1(grammar_text, input_string):
    grammar, start_symbol = parse_grammar(grammar_text)
    first = compute_first(grammar)
    follow = compute_follow(grammar, first, start_symbol)
    parse_table = build_parse_table(grammar, first, follow)

    stack = ["$", start_symbol]
    input_buffer = input_string.split() + ["$"]

    steps = []

    while True:
        stack_top = stack[-1]
        current_input = input_buffer[0]

        steps.append((stack.copy(), input_buffer.copy()))

        if stack_top == current_input == "$":
            return "ACCEPTED", steps

        if stack_top == current_input:
            stack.pop()
            input_buffer.pop(0)

        elif stack_top in grammar:
            if current_input in parse_table[stack_top]:
                production = parse_table[stack_top][current_input]
                stack.pop()

                if production != ["ε"]:
                    for symbol in reversed(production):
                        stack.append(symbol)
            else:
                return "REJECTED", steps
        else:
            return "REJECTED", steps

