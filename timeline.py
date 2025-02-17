import tkinter as tk
import datetime

# Define terms in order
terms = ["Fa24", "Sp25", "Su25", "Fa25", "Sp26", "Su26", "Fa26", "Sp27", "Su27", "Fa27", "Sp28"]
term_dates = [
    datetime.datetime(2024, 9, 1), datetime.datetime(2025, 1, 1), datetime.datetime(2025, 5, 1),
    datetime.datetime(2025, 9, 1), datetime.datetime(2026, 1, 1), datetime.datetime(2026, 5, 1),
    datetime.datetime(2026, 9, 1), datetime.datetime(2027, 1, 1), datetime.datetime(2027, 5, 1),
    datetime.datetime(2027, 9, 1), datetime.datetime(2028, 1, 1)
]

# Get today's date
today = datetime.datetime.today()

# Determine the position of the current term
def get_current_term_position():
    for i in range(len(term_dates) - 1):
        if term_dates[i] <= today < term_dates[i + 1]:
            fraction = (today - term_dates[i]).days / (term_dates[i + 1] - term_dates[i]).days
            return i + fraction
    return len(terms) - 1  # If beyond last term, place at the end

# Create the GUI
root = tk.Tk()
root.title("Graphical Timeline")

canvas_width = 600
canvas_height = 150
timeline_y = canvas_height // 2
padding = 50
dot_radius = 8

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw the timeline
start_x = padding
end_x = canvas_width - padding
step = (end_x - start_x) / (len(terms) - 1)

canvas.create_line(start_x, timeline_y, end_x, timeline_y, width=3)

# Draw term markers
for i, term in enumerate(terms):
    x = start_x + i * step
    canvas.create_oval(x - 5, timeline_y - 5, x + 5, timeline_y + 5, fill="black")
    canvas.create_text(x, timeline_y + 20, text=term, font=("Arial", 10))

# Draw moving dot
position = get_current_term_position()
dot_x = start_x + position * step
dot = canvas.create_oval(dot_x - dot_radius, timeline_y - dot_radius, dot_x + dot_radius, timeline_y + dot_radius, fill="red")

root.mainloop()
