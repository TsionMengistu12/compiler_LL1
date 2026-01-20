from parser.grammar import parse_grammar
from parser.first_follow import compute_first, compute_follow
from parser.parse_table import build_parse_table

def run_ll1(grammar_text, input_string):

    try:
        grammar, start_symbol, _, _ = parse_grammar(grammar_text)
    except ValueError as e:
        return f"Grammar Error: {e}", [], None
    
    first = compute_first(grammar)
    follow = compute_follow(grammar, first, start_symbol)
    parse_table = build_parse_table(grammar, first, follow)

    stack = ["$", start_symbol]
    input_buffer = input_string.strip().split() + ["$"]

    steps = []

    while True:
        stack_top = stack[-1]
        current_input = input_buffer[0]
        action = ""


        if stack_top == current_input == "$":
            steps.append((stack.copy(), input_buffer.copy(), "ACCEPT"))
            return "ACCEPTED", steps, parse_table

        if stack_top == current_input:
            action = f"Match {current_input}"
            stack.pop()
            input_buffer.pop(0)

        elif stack_top in grammar:
            if current_input in parse_table[stack_top]:
                production = parse_table[stack_top][current_input]
                action = f"{stack_top} → {' '.join(production)}"
                stack.pop()

                if production != ["ε"]:
                    for symbol in reversed(production):
                        stack.append(symbol)
            else:
                action = f"Error: no rule for ({stack_top}, {current_input})"
                steps.append((stack.copy(), input_buffer.copy(), action))
                return f"REJECTED: no rules for ({stack_top}, {current_input})", steps, parse_table
        else:
            action = f"Error: unexpected {current_input}"
            steps.append((stack.copy(), input_buffer.copy(), action))
            return f"REJECTED: unexpected symbol '{current_input}' ", steps, parse_table
        
        steps.append((stack.copy(), input_buffer.copy(), action))

