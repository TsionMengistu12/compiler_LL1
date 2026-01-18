import customtkinter as ctk

class InputUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Input String").pack(side="left", padx=10)

        self.entry = ctk.CTkEntry(self, width=300)
        self.entry.pack(side="left", padx=10)

        self.parse_btn = ctk.CTkButton(
            self,
            text="Parse",
            command=self.parse
        )
        self.parse_btn.pack(side="left", padx=10)

    def parse(self):
        grammar = self.master.grammar_ui.get_grammar()
        input_string = self.entry.get()

        self.master.output_ui.display_result(grammar, input_string)