import customtkinter as ctk
from gui.app import LL1App

def main():
    # Configure theme
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Create and run app
    app = LL1App()
    app.mainloop()

if __name__ == "__main__":
    main()
