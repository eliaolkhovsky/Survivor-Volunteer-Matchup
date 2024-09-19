import tkinter as tk
import Window
from tkinter import ttk
import ScrollPageLogic as sl

# main window
root = tk.Tk()
root.title("Volunteer for Holocaust Survivors")
root.geometry(f"{Window.WINDOW_WIDTH}x{Window.WINDOW_HEIGHT}")
root.configure(bg="#e6f2ff")


# canvas
canvas = tk.Canvas(root, bg="#e6f2ff")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#e6f2ff")


scrollable_frame.bind(
   "<Configure>",
   lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)


canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# write from left to right
def set_ltr(widget):
   widget.config(justify="left", anchor="w")


# write in text box
def round_entry(entry):
   entry.config(relief="solid", bd=2, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#66b2ff")


# Label for list of complaints
problems_label = tk.Label(scrollable_frame, text="List of Complaints:", font=("Arial", 14), bg="#e6f2ff")
set_ltr(problems_label)
problems_label.pack(pady=10, anchor="w")


# Scrollable list of common complaints
scroll_frame = tk.Frame(scrollable_frame, bg="#e6f2ff")
scroll_frame.pack(fill="both", expand=True, pady=10, padx=20)


scrollbar = tk.Scrollbar(scroll_frame)
scrollbar.pack(side="right", fill="y")


listbox = tk.Listbox(scroll_frame, yscrollcommand=scrollbar.set, height=7, width=75, justify="left",
                    font=("Arial", 12), bd=2,
                    activestyle="dotbox")
problems = [
   "Health Issues: Assistance with filling medical forms, using medical equipment",
   "Social Isolation: Encouragement and phone calls",
   "Help filling official forms",
   "Emotional and social support"
]



for problem in problems:
   listbox.insert("end", problem)
listbox.pack(side="left", fill="both", expand=True)


scrollbar.config(command=listbox.yview)


# Text box for first and last name
name_frame = tk.Frame(scrollable_frame, bg="#e6f2ff")
name_frame.pack(pady=10, padx=20, anchor="w")


first_name_label = tk.Label(name_frame, text="First Name:", font=("Arial", 14), bg="#e6f2ff")
set_ltr(first_name_label)
first_name_label.grid(row=0, column=0, padx=10)
first_name_entry = tk.Entry(name_frame, width=25, justify="left", bd=2)
round_entry(first_name_entry)
first_name_entry.grid(row=0, column=1)


last_name_label = tk.Label(name_frame, text="Last Name:", font=("Arial", 14), bg="#e6f2ff")
set_ltr(last_name_label)
last_name_label.grid(row=1, column=0, padx=10)
last_name_entry = tk.Entry(name_frame, width=25, justify="left", bd=2)
round_entry(last_name_entry)
last_name_entry.grid(row=1, column=1)


# Text box for place of residence
city_label = tk.Label(name_frame, text="Place: ", font=("Arial", 14), bg="#e6f2ff")
set_ltr(city_label)
city_label.grid(row=2, column=0, padx=10)
city_entry = tk.Entry(name_frame, width=25, justify="left", bd=2)
round_entry(city_entry)
city_entry.grid(row=2, column=1)

city_label2 = tk.Label(name_frame, text="Place: ", font=("Arial", 14), bg="#e6f2ff")
set_ltr(city_label2)
city_label2.grid(row=3, column=0, padx=10)
city_entry2 = tk.Entry(name_frame, width=25, justify="left", bd=2)
round_entry(city_entry2)
city_entry2.grid(row=3, column=1)

# Gender selection
gender_label = tk.Label(scrollable_frame, text="Gender: ", font=("Arial", 14), bg="#e6f2ff")
set_ltr(gender_label)
gender_label.pack(pady=10, anchor="w")


gender_frame = tk.Frame(scrollable_frame, bg="#e6f2ff")
gender_frame.pack(anchor="w", padx=20)


gender_var = tk.StringVar(value="")
male_checkbox = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#e6f2ff",
                              font=("Arial", 12), anchor="w")
female_checkbox = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#e6f2ff",
                                font=("Arial", 12), anchor="w")


male_checkbox.grid(row=0, column=0, padx=10)
female_checkbox.grid(row=0, column=1, padx=10)


# Age selector
age_label = tk.Label(scrollable_frame, text="Age:", font=("Arial", 14), bg="#e6f2ff")
set_ltr(age_label)
age_label.pack(pady=10, anchor="w")


age_spinbox = tk.Spinbox(scrollable_frame, from_=1, to=99, width=10, justify="left", font=("Arial", 12))
age_spinbox.pack(pady=5, anchor="w")


# Send button with colored background
button = tk.Button(scrollable_frame, text="Send", font=("Arial", 14), bg="#28a745", fg="white", command=lambda: print(
   f"First Name: {first_name_entry.get()}, Last Name: {last_name_entry.get()}, Place: {city_entry.get()}, Age: {age_spinbox.get()}, Gender: {gender_var.get()}, Problem: {listbox.get(listbox.curselection())}"
   f""))
button.pack(pady=20, padx=20, ipadx=10, ipady=5)


gender_label.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("gender")))

problems_label.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech(problems)))


first_name_label.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("First name")))


last_name_label.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("Last name")))

city_label.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("place")))
city_label2.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("place")))

age_spinbox.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("age")))


male_checkbox.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("male")))

female_checkbox.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("female")))

button.bind('<Enter>', func=lambda e: button.config(
        background=sl.txt_to_speech("send")))


# Start main loop
root.mainloop()

