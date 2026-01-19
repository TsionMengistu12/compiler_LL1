import customtkinter as ctk

class GrammarUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self,
                     text="Enter Grammar Rules (one rule per line)",
                     font=("Arial", 14, "bold")).pack(pady=5)

        self.textbox = ctk.CTkTextbox(self, width=350, height=450)
        self.textbox.pack(padx=10, pady=10)

        # self.textbox.insert("1.0",
        #     "E -> T E'\n"
        #     "E' -> + T E' | ε\n"
        #     "T -> F T'\n"
        #     "T' -> * F T' | ε\n"
        #    "F -> ( E ) | id"
        # )

    def get_grammar(self):
        return self.textbox.get("1.0", "end").strip()