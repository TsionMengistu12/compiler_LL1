import customtkinter as ctk


class ParseTableUi(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#0f172a", border_color="#475569", border_width=1, corner_radius=8)

        self.table_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            label_text="",
            label_font=None
        )
        # A bit more padding makes the table feel less cramped.
        self.table_frame.pack(fill="both", expand=True, padx=14, pady=14)

    def display(self, parse_table):
        for w in self.table_frame.winfo_children():
            w.destroy()

        if not parse_table:
            ctk.CTkLabel(
                self.table_frame,
                text="No parse table generated yet",
                font=("Segoe UI", 14),
                text_color="#64748b"
            ).pack(pady=20)
            return

        terminals = sorted({t for row in parse_table.values() for t in row})

        # Make the grid responsive (so resizing the window feels good).
        total_cols = len(terminals) + 1  # +1 for NT column
        for c in range(total_cols):
            self.table_frame.grid_columnconfigure(c, weight=1, minsize=120)
        self.table_frame.grid_columnconfigure(0, weight=0, minsize=90)  # NT column

        # Header row - Non-Terminal column
        header_cell = ctk.CTkFrame(self.table_frame, fg_color="#1e293b", corner_radius=6)
        header_cell.grid(row=0, column=0, padx=4, pady=4, sticky="nsew")

        ctk.CTkLabel(
            header_cell,
            text="NT \\ T",
            font=("Segoe UI", 15, "bold"),
            text_color="#e0e7ff"
        ).pack(padx=12, pady=12)

        # Terminal headers
        for c, t in enumerate(terminals, start=1):
            header_cell = ctk.CTkFrame(self.table_frame, fg_color="#1e293b", corner_radius=6)
            header_cell.grid(row=0, column=c, padx=4, pady=4, sticky="nsew")

            ctk.CTkLabel(
                header_cell,
                text=t,
                font=("Segoe UI", 15, "bold"),
                text_color="#e0e7ff"
            ).pack(padx=12, pady=12)

        # Table body
        for r, nt in enumerate(parse_table, start=1):
            # Non-terminal label
            nt_cell = ctk.CTkFrame(self.table_frame, fg_color="#1a1f2e", corner_radius=6)
            nt_cell.grid(row=r, column=0, padx=4, pady=4, sticky="nsew")

            ctk.CTkLabel(
                nt_cell,
                text=nt,
                font=("Segoe UI", 15, "bold"),
                text_color="#cbd5e1"
            ).pack(padx=12, pady=12)

            # Production cells
            for c, t in enumerate(terminals, start=1):
                prod = parse_table[nt].get(t)
                cell_text = " ".join(prod) if prod else "—"
                
                bg_color = "#064e3b" if prod else "#1a1f2e"
                text_color = "#86efac" if prod else "#64748b"

                cell = ctk.CTkFrame(self.table_frame, fg_color=bg_color, corner_radius=6)
                cell.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

                ctk.CTkLabel(
                    cell,
                    text=cell_text,
                    wraplength=180,
                    font=("Courier New", 15),
                    text_color=text_color
                ).pack(padx=12, pady=12)
