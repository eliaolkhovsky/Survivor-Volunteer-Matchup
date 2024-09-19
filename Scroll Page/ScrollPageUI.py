import tkinter as tk
from tkinter import ttk
import Window

# main window
root = tk.Tk()
root.title("התנדבות למען ניצולי שואה")
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


# write from right to left
def set_rtl(widget):
    widget.config(justify="right", anchor="e")


# write in text box
def round_entry(entry):
    entry.config(relief="solid", bd=2, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#66b2ff")


# כותרת עליונה עם רקע צבעוני
title = tk.Label(scrollable_frame, text=" !ברוך הבא לדף ההתנדבות למען ניצולי שואה ", font=("Arial", 24, "bold"),
                 bg="#3b5998", fg="white")
set_rtl(title)
title.pack(fill="x", pady=20)

# תיבת טקסט להוספת שם פרטי ושם משפחה
name_frame = tk.Frame(scrollable_frame, bg="#e6f2ff")
name_frame.pack(pady=10, padx=20, anchor="e")

first_name_label = tk.Label(name_frame, text=":שם פרטי", font=("Arial", 14), bg="#e6f2ff")
set_rtl(first_name_label)
first_name_label.grid(row=0, column=1, padx=10)
first_name_entry = tk.Entry(name_frame, width=25, justify="right", bd=2)
round_entry(first_name_entry)
first_name_entry.grid(row=0, column=0)

last_name_label = tk.Label(name_frame, text=":שם משפחה", font=("Arial", 14), bg="#e6f2ff")
set_rtl(last_name_label)
last_name_label.grid(row=1, column=1, padx=10)
last_name_entry = tk.Entry(name_frame, width=25, justify="right", bd=2)
round_entry(last_name_entry)
last_name_entry.grid(row=1, column=0)

# תיבת טקסט להוספת מקום מגורים
city_label = tk.Label(name_frame, text=":מקום מגורים", font=("Arial", 14), bg="#e6f2ff")
set_rtl(city_label)
city_label.grid(row=2, column=1, padx=10)
city_entry = tk.Entry(name_frame, width=25, justify="right", bd=2)
round_entry(city_entry)
city_entry.grid(row=2, column=0)

# בחירת מגדר
gender_label = tk.Label(scrollable_frame, text=":בחר מגדר", font=("Arial", 14), bg="#e6f2ff")
set_rtl(gender_label)
gender_label.pack(pady=10, anchor="e")

gender_frame = tk.Frame(scrollable_frame, bg="#e6f2ff")
gender_frame.pack(anchor="e", padx=20)

gender_var = tk.StringVar(value="")
male_checkbox = tk.Radiobutton(gender_frame, text="זכר", variable=gender_var, value="זכר", bg="#e6f2ff",
                               font=("Arial", 12), anchor="w")
female_checkbox = tk.Radiobutton(gender_frame, text="נקבה", variable=gender_var, value="נקבה", bg="#e6f2ff",
                                 font=("Arial", 12), anchor="w")

male_checkbox.grid(row=0, column=2, padx=10)
female_checkbox.grid(row=0, column=1, padx=10)

# סקרולר גילאים
age_label = tk.Label(scrollable_frame, text=":גיל", font=("Arial", 14), bg="#e6f2ff")
set_rtl(age_label)
age_label.pack(pady=10, anchor="e")

age_spinbox = tk.Spinbox(scrollable_frame, from_=1, to=99, width=10, justify="right", font=("Arial", 12))
age_spinbox.pack(pady=5, anchor="e")

# תיבת טקסט לבעיות שעלולות להיווצר
problems_label = tk.Label(scrollable_frame, text="?באיזו בעיה תרצה לעזור", font=("Arial", 14), bg="#e6f2ff")
set_rtl(problems_label)
problems_label.pack(pady=10, anchor="e")

# רשימת בעיות נפוצות לניצולי שואה מבוגרים עם צבעים
scroll_frame = tk.Frame(scrollable_frame, bg="#e6f2ff")
scroll_frame.pack(fill="both", expand=True, pady=10, padx=20)

scrollbar = tk.Scrollbar(scroll_frame)
scrollbar.pack(side="left", fill="y")

listbox = tk.Listbox(scroll_frame, yscrollcommand=scrollbar.set, height=5, justify="right", font=("Arial", 12), bd=2,
                     activestyle="dotbox")
problems = [
    "בעיות טכנולוגיות: שימוש במחשב, טלפון נייד, אינטרנט",
    "בעיות בריאותיות: סיוע במילוי טפסים רפואיים, שימוש בציוד רפואי",
    "בדידות חברתית: עידוד ושיחות טלפון",
    "סיוע במילוי טפסים רשמיים",
    "תמיכה נפשית וחברתית"
]

for problem in problems:
    listbox.insert("end", problem)
listbox.pack(side="right", fill="both", expand=True)

scrollbar.config(command=listbox.yview)

# כפתור שלח עם רקע צבעוני
button = tk.Button(scrollable_frame, text="שלח", font=("Arial", 14), bg="#28a745", fg="white", command=lambda: print(
    f"שם פרטי: {first_name_entry.get()}, שם משפחה: {last_name_entry.get()}, מקום מגורים: {city_entry.get()}, גיל: {age_spinbox.get()}, מגדר: {gender_var.get()}, בעיה: {listbox.get(listbox.curselection())}"))
button.pack(pady=20, padx=20, ipadx=10, ipady=5)

# Checkbox to indicate if the user is a volunteer or needs help
status_var = tk.StringVar()
volunteer_checkbox = tk.Checkbutton(scrollable_frame, text="אני מתנדב", variable=status_var, onvalue="מתנדב",
                                    offvalue="זקוק לעזרה", bg="#e6f2ff", font=("Arial", 12), anchor="w")
volunteer_checkbox.pack(pady=5, anchor="e")

# הוספת המון אובייקטים נוספים להדגמה של גלילה
for i in range(50):
    tk.Label(scrollable_frame, text=f"אובייקט נוסף {i + 1}", font=("Arial", 12), bg="#e6f2ff").pack(pady=5)

# התחלת הלולאה הראשית
root.mainloop()
