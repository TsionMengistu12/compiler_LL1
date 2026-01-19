import customtkinter as ctk
from gui.grammar_ui import GrammarUi
from gui.input_ui import InputUi
from gui.output_ui import OutputUi
from gui.parse_table_ui import ParseTableUi


class LL1App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LL(1) Parser Visualizer")
        self.geometry("1400x900")
        self.minsize(1200, 700)

        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Header frame
        header_frame = ctk.CTkFrame(self, fg_color="#1e40af", corner_radius=0)
        header_frame.pack(fill="x", padx=0, pady=0)

        header_label = ctk.CTkLabel(
            header_frame,
            text="LL(1) Parser Visualizer",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        )
        header_label.pack(pady=16)

        # Container frame for all content
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Grammar section
        grammar_label = ctk.CTkLabel(
            container,
            text="Grammar Rules",
            font=("Segoe UI", 14, "bold"),
            text_color="#e0e7ff"
        )
        grammar_label.pack(anchor="w", pady=(0, 8))

        self.grammar_ui = GrammarUi(container)
        self.grammar_ui.pack(fill="x", padx=0, pady=(0, 16))

        # Input and controls section
        controls_label = ctk.CTkLabel(
            container,
            text="Parse Input",
            font=("Segoe UI", 14, "bold"),
            text_color="#e0e7ff"
        )
        controls_label.pack(anchor="w", pady=(0, 8))

        self.input_ui = InputUi(container)
        self.input_ui.pack(fill="x", padx=0, pady=(0, 16))

        # Main content section (2 columns)
        self.main_frame = ctk.CTkFrame(container, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.grid_columnconfigure((0, 1), weight=1)

        # Output section label
        output_label = ctk.CTkLabel(
            self.main_frame,
            text="Parsing Steps",
            font=("Segoe UI", 14, "bold"),
            text_color="#e0e7ff"
        )
        output_label.grid(row=0, column=0, sticky="w", pady=(0, 8))

        # Parse table section label
        table_label = ctk.CTkLabel(
            self.main_frame,
            text="LL(1) Parse Table",
            font=("Segoe UI", 14, "bold"),
            text_color="#e0e7ff"
        )
        table_label.grid(row=0, column=1, sticky="w", pady=(0, 8), padx=(16, 0))

        # Output UI
        self.output_ui = OutputUi(self.main_frame)
        self.output_ui.grid(row=1, column=0, sticky="nsew", padx=(0, 8), pady=0)

        # Parse table UI
        self.parse_table_ui = ParseTableUi(self.main_frame)
        self.parse_table_ui.grid(row=1, column=1, sticky="nsew", padx=(8, 0), pady=0)

        # Configure grid weights
        self.main_frame.grid_rowconfigure(1, weight=1)
