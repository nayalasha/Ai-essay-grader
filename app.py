import customtkinter as ctk

window = ctk.CTk()
window.title("AI Essay Grader")
window.geometry("1280x720")


# ---------------- FUNCTIONS ---------------- #

def clear_text():
    text_box.delete("1.0", "end")
    result_label.configure(text="")


def grade_essay():
    essay = text_box.get("1.0", "end").strip()

    if essay:
        word_count = len(essay.split())

        # SIMPLE GRADING LOGIC
        if word_count > 400:
            grade = "A"
        elif word_count > 200:
            grade = "B"
        else:
            grade = "C"

        result_label.configure(
            text=f"Grade: {grade} | Words: {word_count}"
        )

    else:
        result_label.configure(text="Please enter an essay.")


# ---------------- TITLE ---------------- #

ctk.CTkLabel(
    window,
    text="AI Essay Grader",
    font=ctk.CTkFont(size=40, weight="bold")
).pack(pady=10)


# ---------------- MAIN FRAME ---------------- #

main_frame = ctk.CTkFrame(window)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)


# ---------------- TEXT BOX ---------------- #

text_box = ctk.CTkTextbox(main_frame, width=800, height=600)
text_box.pack(side="left", padx=20, pady=20)


# ---------------- SIDE PANEL ---------------- #

side_frame = ctk.CTkFrame(main_frame)
side_frame.pack(side="right", padx=20, pady=20)


ctk.CTkLabel(
    side_frame,
    text="Enter Essay → Click Grade",
    font=ctk.CTkFont(size=18)
).pack(pady=10)


# ---------------- BUTTONS ---------------- #

ctk.CTkButton(
    side_frame,
    text="Grade Essay",
    command=grade_essay,
    width=200,
    height=50
).pack(pady=10)


ctk.CTkButton(
    side_frame,
    text="Clear",
    command=clear_text,
    width=200,
    height=50
).pack(pady=10)


# ---------------- RESULT ---------------- #

result_label = ctk.CTkLabel(
    side_frame,
    text="",
    font=ctk.CTkFont(size=18)
)
result_label.pack(pady=20)


# ---------------- RUN ---------------- #

window.mainloop()