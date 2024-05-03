from tkinter import *
import math as m
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
delay = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(delay)
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps in (1, 3, 5, 7):
        count_down(work_sec)
        label.config(text="Work",fg=GREEN)
    elif reps in (2, 4, 6):
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK, bg=YELLOW)
    elif reps == 8:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED, bg=YELLOW)
        reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = m.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global delay
        delay = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = m.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="E:/Python/Course/pomodoro/tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer = canvas.create_text(102, 130, text=(
    "00:00"), font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start = Button(text="Start", font=(FONT_NAME, 12), command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 12), command=reset_timer)
reset.grid(column=2, row=2)

tick = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)


window.mainloop()
