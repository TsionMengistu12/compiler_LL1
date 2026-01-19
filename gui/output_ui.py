# output_ui.py
import customtkinter as ctk
from parser.ll1_parser import run_ll1


class OutputUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#0f172a", border_color="#475569", border_width=1, corner_radius=8)

        # Container for scrollable frame and result
        self.steps_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            label_text="",
            label_font=None
        )
        self.steps_frame.pack(fill="both", expand=True, padx=12, pady=12)

        # Result label
        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI", 12, "bold"),
            text_color="#22c55e"
        )
        self.result_label.pack(pady=12)

    def display_result(self, grammar_text, input_string):
        for w in self.steps_frame.winfo_children():
            w.destroy()

        try:
            result, steps, parse_table = run_ll1(grammar_text, input_string)

            headers = ["Step", "Stack", "Input", "Action"]
            widths = [50, 200, 200, 240]

            # Header row
            for c, h in enumerate(headers):
                ctk.CTkLabel(
                    self.steps_frame,
                    text=h,
                    font=("Segoe UI", 14, "bold"),
                    text_color="#e0e7ff",
                    width=widths[c]
                ).grid(row=0, column=c, padx=6, pady=8, sticky="w")

            # Separator line
            sep = ctk.CTkFrame(self.steps_frame, height=1, fg_color="#334155")
            sep.grid(row=1, column=0, columnspan=4, sticky="ew", padx=0, pady=4)

            # Data rows
            for i, (stack, buffer, action) in enumerate(steps, start=2):
                bg_color = "#1e293b" if i % 2 == 0 else "#0f172a"

                values = [
                    str(i - 1),
                    " ".join(stack),
                    " ".join(buffer),
                    action
                ]

                for c, v in enumerate(values):
                    ctk.CTkLabel(
                        self.steps_frame,
                        text=v,
                        width=widths[c],
                        font=("Courier New", 14),
                        text_color="#cbd5e1",
                        anchor="w"
                    ).grid(row=i, column=c, padx=6, pady=4, sticky="w")

            # Update result
            color = "#22c55e" if result == "ACCEPTED" else "#ef4444"
            status_text = f"✓ Result: {result}" if result == "ACCEPTED" else f"✗ Result: {result}"
            self.result_label.configure(text=status_text, text_color=color)

            self.master.master.parse_table_ui.display(parse_table)
        except Exception as e:
            self.result_label.configure(
                text=f"Error: {str(e)}",
                text_color="#ef4444"
            )
