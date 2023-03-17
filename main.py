import tkinter as tk
from tkinter import ttk
import time

def validate_time(time_str):
    try:
        time.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def submit():
    start_date = f"{start_year.get()}-{start_month.get():0>2}-{start_day.get():0>2}"
    end_date = f"{end_year.get()}-{end_month.get():0>2}-{end_day.get():0>2}"
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    room_code = room_code_entry.get()
    print(f"Start date: {start_date}")
    print(f"End date: {end_date}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Room code: {room_code}")

root = tk.Tk()
root.geometry("400x200")

form_frame = ttk.Frame(root, padding=20)
form_frame.pack(fill="both", expand=True)

start_date_label = ttk.Label(form_frame, text="Start date:")
start_date_label.grid(column=0, row=0, sticky=tk.W)

start_day = ttk.Combobox(form_frame, values=[i for i in range(1, 32)], width=2)
start_day.grid(column=1, row=0, sticky=tk.W)

start_month_year_frame = ttk.Frame(form_frame)
start_month_year_frame.grid(column=1, row=0)

start_month = ttk.Combobox(start_month_year_frame, values=[i for i in range(1, 13)], width=2)
start_month.pack(side="left")

start_year = ttk.Combobox(start_month_year_frame, values=[i for i in range(2023, 2031)], width=4)
start_year.pack(side="left", padx=(5,0))

end_date_label = ttk.Label(form_frame, text="End date: ")
end_date_label.grid(column=0, row=1, sticky=tk.W)

end_day = ttk.Combobox(form_frame, values=[i for i in range(1, 32)], width=2)
end_day.grid(column=1, row=1, sticky=tk.W)

end_month_year_frame = ttk.Frame(form_frame)
end_month_year_frame.grid(column=1, row=1)

end_month = ttk.Combobox(end_month_year_frame, values=[i for i in range(1, 13)], width=2)
end_month.pack(side="left")

end_year = ttk.Combobox(end_month_year_frame, values=[i for i in range(2023, 2031)], width=4)
end_year.pack(side="left", padx=(5,0))

start_time_label = ttk.Label(form_frame, text="Start time: ")
start_time_label.grid(column=0, row=2, sticky=tk.W)

start_time_entry = ttk.Entry(form_frame, validate="key", validatecommand=(validate_time, '%P'))
start_time_entry.grid(column=1, row=2)

end_time_label = ttk.Label(form_frame, text="End time: ")
end_time_label.grid(column=0, row=3, sticky=tk.W)

end_time_entry = ttk.Entry(form_frame, validate="key", validatecommand=(validate_time, '%P'))
end_time_entry.grid(column=1, row=3)

room_code_label = ttk.Label(form_frame, text="Room code: ")
room_code_label.grid(column=0, row=4, sticky=tk.W)

room_code_entry = ttk.Entry(form_frame)
room_code_entry.grid(column=1, row=4)

# Create a button to submit the form
submit_button = ttk.Button(form_frame, text="Submit", command=submit)
submit_button.grid(column=0, row=7, pady=(20, 0), columnspan=2)

root.mainloop()