import customtkinter as ctk
from gui.app import LL1App
##### tester on weather the customtkinter works
# # ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("green")

# app = ctk.CTk()
# app.geometry("400x400")

# ctk.CTkLabel(app, text="Checking if this works?!").pack(pady=20)
# app.mainloop()

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = LL1App()
    app.mainloop()

if __name__ == "__main__":
    main()
