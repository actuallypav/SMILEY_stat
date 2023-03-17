import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime

def validate_time_in_range():
    dt_start = datetime(year = int(start_year.get()), month = int(start_month.get()), day = int(start_day.get()), hour = int(start_time_hours.get()), minute = int(start_time_minutes.get()))
    dt_end = datetime(year = int(end_year.get()), month = int(end_month.get()), day = int(start_day.get()), hour = int(end_time_hours.get()), minute = int(end_time_minutes.get()))
    # is start time smaller than end time
    if dt_start < dt_end:
        return True
    else:
        return False

def submit():
    if validate_time_in_range() == True:
        print("success")
    else:
        print("fail")

root = tk.Tk()
root.geometry("400x200")

form_frame = ttk.Frame(root, padding=20)
form_frame.pack(fill="both", expand=True)

start_date_label = ttk.Label(form_frame, text="Start date:")
start_date_label.grid(column=0, row=0, sticky=tk.W)

start_day = ttk.Combobox(form_frame, values=[i for i in range(1, 32)], width=2, state="readonly")
start_day.grid(column=1, row=0, sticky=tk.W)

start_month_year_frame = ttk.Frame(form_frame)
start_month_year_frame.grid(column=1, row=0)

start_month = ttk.Combobox(start_month_year_frame, values=[i for i in range(1, 13)], width=2, state="readonly")
start_month.pack(side="left")

start_year = ttk.Combobox(start_month_year_frame, values=[i for i in range(2023, 2031)], width=4, state="readonly")
start_year.pack(side="left", padx=(5,0))

end_date_label = ttk.Label(form_frame, text="End date: ")
end_date_label.grid(column=0, row=1, sticky=tk.W)

end_day = ttk.Combobox(form_frame, values=[i for i in range(1, 32)], width=2, state="readonly")
end_day.grid(column=1, row=1, sticky=tk.W)

end_month_year_frame = ttk.Frame(form_frame)
end_month_year_frame.grid(column=1, row=1)

end_month = ttk.Combobox(end_month_year_frame, values=[i for i in range(1, 13)], width=2, state="readonly")
end_month.pack(side="left")

end_year = ttk.Combobox(end_month_year_frame, values=[i for i in range(2023, 2031)], width=4, state="readonly")
end_year.pack(side="left", padx=(5,0))





start_time_label = ttk.Label(form_frame, text="Start time: ")
start_time_label.grid(column=0, row=2)

start_time_frame = ttk.Frame(form_frame)
start_time_frame.grid(column=1, row=2, sticky=tk.W)

start_time_hours = ttk.Combobox(start_time_frame, values=[i for i in range(1, 25)], width=2, state="readonly")
start_time_hours.pack(side="left")

start_time_minutes = ttk.Combobox(start_time_frame, values=[i for i in range(0, 60)], width=2, state="readonly")
start_time_minutes.pack(side="left", padx=(5,0))

# start_time_entry = ttk.Entry(form_frame, command=lambda: validate_time(start_time_entry.get()))
# start_time_entry.grid(column=1, row=2)

end_time_label = ttk.Label(form_frame, text="End time: ")
end_time_label.grid(column=0, row=3)

end_time_frame = ttk.Frame(form_frame)
end_time_frame.grid(column=1, row=3, sticky=tk.W)

end_time_hours = ttk.Combobox(end_time_frame, values=[i for i in range(1, 25)], width=2, state="readonly")
end_time_hours.pack(side="left")

end_time_minutes = ttk.Combobox(end_time_frame, values=[i for i in range(0, 60)], width=2, state="readonly")
end_time_minutes.pack(side="left", padx=(5,0))

# end_time_entry = ttk.Entry(form_frame)
# end_time_entry.grid(column=1, row=3)

room_code_label = ttk.Label(form_frame, text="Room code: ")
room_code_label.grid(column=0, row=4, sticky=tk.W)

room_code_entry = ttk.Entry(form_frame)
room_code_entry.grid(column=1, row=4)

# Create a button to submit the form
submit_button = ttk.Button(form_frame, text="Submit", command=submit)
submit_button.grid(column=0, row=7, pady=(20, 0), columnspan=2)

root.mainloop()