import customtkinter as ctk
from parser.ll1_parser import run_ll1
from gui.parse_table_ui import ParseTableUi


class InputUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        # Input frame
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.pack(fill="x", padx=0)

        # Input entry with label
        entry_label = ctk.CTkLabel(
            input_frame,
            text="Input String:",
            font=("Segoe UI", 11),
            text_color="#cbd5e1"
        )
        entry_label.pack(side="left", padx=(0, 12))

        self.entry = ctk.CTkEntry(
            input_frame,
            width=300,
            font=("Courier New", 11),
            fg_color="#0f172a",
            text_color="#e0e7ff",
            border_color="#475569",
            border_width=1,
            placeholder_text="Enter input string (e.g., (id+id)*id)"
        )
        self.entry.pack(side="left", padx=(0, 12), fill="x", expand=True)

        # Parse button
        self.parse_btn = ctk.CTkButton(
            input_frame,
            text="Parse",
            command=self.parse,
            font=("Segoe UI", 11, "bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            width=100,
            height=36
        )
        self.parse_btn.pack(side="left", padx=(0, 8))

        # Show Parse Table button
        self.table_btn = ctk.CTkButton(
            input_frame,
            text="Show Parse Table",
            command=self.show_table,
            font=("Segoe UI", 11, "bold"),
            fg_color="#7c3aed",
            hover_color="#6d28d9",
            width=130,
            height=36
        )
        self.table_btn.pack(side="left", padx=0)

    def parse(self):
        grammar = self.master.master.grammar_ui.get_grammar()
        input_string = self.entry.get()

        self.master.master.output_ui.display_result(grammar, input_string)

    def show_table(self):
        grammar = self.master.master.grammar_ui.get_grammar()
        input_string = self.entry.get()

        # Run parser just to get the parse table
        _, _, parse_table = run_ll1(grammar, input_string)

        # Update the existing parse table view
        self.master.master.parse_table_ui.display(parse_table)
