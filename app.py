import customtkinter as ctk

window = ctk.CTk()
window.title("Ai essay grader")
window.geometry("1280x720")


ctk.CTkLabel(window, text="AI Essay Grader!",
              font=ctk.CTkFont(size=40, weight="bold")).pack(pady=10)


listbox = ctk.CTkTextbox(window, width=800, height=700,
                         font=ctk.CTkFont(size=16),
                         scrollbar_button_color="lightgray")
listbox.pack(pady=20, side="left", padx=20)



window.mainloop()