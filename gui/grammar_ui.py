import customtkinter as ctk

class GrammarUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        # Input instruction
        instruction = ctk.CTkLabel(
            self,
            text="Enter grammar rules (one rule per line, e.g., E -> T E' | ε)",
            font=("Segoe UI", 14),
            text_color="#a0aec0"
        )
        instruction.pack(pady=(0, 10), anchor="w")

        # Textbox with improved styling
        self.textbox = ctk.CTkTextbox(
            self,
            width=350,
            height=100,
            font=("Courier New", 14),
            fg_color="#0f172a",
            text_color="#e0e7ff",
            border_color="#475569",
            border_width=1
        )
        self.textbox.pack(fill="both", expand=True, pady=0)

        # # Placeholder example
        # self.textbox.insert("1.0",
        #     "E -> T E'\n"
        #     "E' -> + T E' | ε\n"
        #     "T -> F T'\n"
        #     "T' -> * F T' | ε\n"
        #     "F -> ( E ) | id"
        # )

    def get_grammar(self):
        return self.textbox.get("1.0", "end").strip()
