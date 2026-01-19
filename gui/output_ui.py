import customtkinter as ctk
from parser.ll1_parser import run_ll1

class OutputUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Output", font=("Arial", 14, "bold")).pack(pady=5)

        self.output = ctk.CTkTextbox(self, width=450, height=450)
        self.output.pack(padx=10, pady=10)


    def display_result(self, grammar_text, input_string):
        result, steps = run_ll1(grammar_text, input_string)

        self.output.delete("1.0", "end")
        self.output.insert("end", f"Result: {result}\n\n")

        for i, (stack, buffer) in enumerate(steps, start=1):
            self.output.insert("end",f"step {i}:\n" 
                               f"Stack: {stack}     " 
                               f"Input: {buffer}\n") 