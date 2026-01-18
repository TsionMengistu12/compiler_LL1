import customtkinter as ctk

class GrammarUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Grammar Rules").pack(pady=5)

        self.textbox = ctk.CTkTextbox(self, width=300, height=400)
        self.textbox.pack(padx=10, pady=10)

        self.textbox.insert("1.0",
            "E -> T E'\nE' -> + T E' | ε\nT -> F T'\nT' -> * F T' | ε\nF -> ( E ) | id"
        )

    def get_grammar(self):
        return self.textbox.get("1.0", "end").strip()