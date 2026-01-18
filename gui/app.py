import customtkinter as ctk

from gui.grammar_ui import GrammarUi
from gui.input_ui import InputUi
from gui.output_ui import OutputUi

class LL1App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LL(1) Parser")
        self.geometry("900x600")

        self.grammar_ui = GrammarUi(self)
        self.grammar_ui.pack(side="left", fill="both", expand=True, padx=20, pady= 20)

        self.input_ui = InputUi(self)
        self.input_ui.pack(side="top", fill="x", padx=20)

        self.output_ui = OutputUi(self)
        self.output_ui.pack(side="right", fill="both",expand=True, padx=20, pady=20)