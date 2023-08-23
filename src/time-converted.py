import tkinter as tk


def time_converter(hours, minutes, period):
    if (period == "am" or period == "pm") and (minutes <= 59) and (0 <= hours <= 12):
        if period == "am" and hours > 11:
            return f"{hours-12:02d}:{minutes:02d} Hours"
        elif period == "pm":
            if hours == 12:
                return f"{hours:02d}:{minutes:02d} Hours"
            elif hours < 12:
                return f"{hours + 12:02d}:{minutes:02d} Hours"
            elif hours > 11:
                return f"{hours-12:02d}:{minutes:02d} Hours"
        else:
            return f"{hours:02d}:{minutes:02d} Hours"
    else:
        return "NOT A VALID HOUR"


def convert_and_display():
    hours_input = hours_entry.get()
    minutes_input = minutes_entry.get()
    period = period_entry.get().lower()

    if hours_input == "" or minutes_input == "":
        result = "Fields cannot be Empty !!"
    else:
        hours = int(hours_input)
        minutes = int(minutes_input)
        result = time_converter(hours, minutes, period)
    result_label.config(text=result)


# Create the main window
root = tk.Tk()
root.title("Time Converter")
root.geometry("300x300")

# Create entry widgets for user input
hours_label = tk.Label(root, text="Hours:")
hours_label.pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

period_label = tk.Label(root, text="Period (am/pm):")
period_label.pack()
period_entry = tk.Entry(root)
period_entry.pack()

# Button to convert and display
convert_button = tk.Button(root, text="Convert", command=convert_and_display)
convert_button.pack(padx=15, pady=10)

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main event loop
root.mainloop()  