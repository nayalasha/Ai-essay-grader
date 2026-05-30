import customtkinter as ctk
from streamlit import button

window = ctk.CTk()
window.title("Ai essay grader")
window.geometry("1280x720")

#-------Def--------
def clear_text():
    listbox.delete("1.0", "end")

def grade_essay():
    essay = listbox.get("1.0", "end").strip()
    if essay:
        # Here you would implement your AI grading logic
        # For demonstration, we'll just return a dummy grade
        grade = "A"  # Replace with actual grading logic
        result = f"Essay Grade: {grade}"
    else:
        result = "Please enter an essay to grade."
    
    listbox.delete("1.0", "end")
    listbox.insert("1.0", result)

#-------Labels---------
ctk.CTkLabel(window, text="AI Essay Grader!",
              font=ctk.CTkFont(size=40, weight="bold")).pack(pady=10)

#-------BOX---------
box_frame = ctk.CTkFrame(window)
box_frame.pack(pady=10)
ctk.CTkLabel(box_frame, text="Enter your essay below:",
                font=ctk.CTkFont(size=20)).pack()

box_frame2 = ctk.CTkFrame(window)
box_frame2.pack(pady=10, side="right", padx=20)

#-------Text Box---------
listbox = ctk.CTkTextbox(window, width=800, height=700,
                         font=ctk.CTkFont(size=16),
                         scrollbar_button_color="lightgray")
listbox.pack(pady=20, side="left", padx=20)

#-------Buttons---------
button_frame = ctk.CTkFrame(window)
button_frame.pack(pady=20, side="right", padx=20)
button1 = ctk.CTkButton(button_frame, text="Grade Essay",
                        font=ctk.CTkFont(size=16),
                        width=200, height=50)
button1.pack(pady=10)


button2 = ctk.CTkButton(button_frame, text="Clear",
                        font=ctk.CTkFont(size=16),
                        width=200, height=50)

button2.configure(command=clear_text)

button2.pack(pady=10)



window.mainloop()