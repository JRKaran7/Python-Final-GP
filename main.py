import tkinter as tk
import turtle
from tkinter import *
import random as ran
from tkinter import ttk
import pyttsx3

start = Tk()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
text_val = "Welcome to JKJ Mini-Games"
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)
engine.say(text_val)
engine.runAndWait()


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Application")

        self.color = "black"
        self.eraser_color = "white"

        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack()

        self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

        self.color_label = tk.Label(root, text="Select Color:")
        self.color_label.pack()

        self.color_palette = [
            "black", "red", "green", "blue", "yellow", "purple", "brown", "orange"
        ]

        self.color_buttons = []
        for color in self.color_palette:
            button = tk.Button(root, bg=color, width=2, height=1, command=lambda c=color: self.set_color(c))
            button.pack(side=tk.LEFT)
            self.color_buttons.append(button)

        self.eraser_button = tk.Button(root, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack()

        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)

        self.last_x, self.last_y = None, None
        self.pen_size = 2
        self.is_eraser = False

    def set_color(self, color):
        self.color = color
        self.is_eraser = False

    def use_eraser(self):
        self.color = self.eraser_color
        self.is_eraser = True

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_paint(self, event):
        self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        x, y = event.x, event.y

        if self.last_x and self.last_y:
            if not self.is_eraser:
                self.canvas.create_line(
                    self.last_x, self.last_y, x, y,
                    fill=self.color, width=self.pen_size, capstyle=tk.ROUND, smooth=tk.TRUE
                )
            else:
                self.canvas.create_line(
                    self.last_x, self.last_y, x, y,
                    fill=self.color, width=self.pen_size * 2, capstyle=tk.ROUND, smooth=tk.TRUE
                )

        self.last_x, self.last_y = x, y


def paint():
    root = tk.Tk()

    def goback():
        root.withdraw()
        start.deiconify()

    tk.Button(root, text='Back', command=goback).pack()
    PaintApp(root)
    root.mainloop()


class GuessTheNumber:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.random_number = ran.randint(1, 100)
        self.tries_left = 5

        self.label = Label(master, text="Guess the number (between 1 and 100):")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.submit_button = Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

        self.try_label = Label(master, text=f"Tries left: {self.tries_left}")
        self.try_label.pack()

        self.restart_button = Button(master, text="Play Again", command=self.restart_game, state=DISABLED)
        self.restart_button.pack()

    def check_guess(self):
        user_guess = self.entry.get()

        if not user_guess.isdigit():
            self.result_label.config(text="Please enter a valid number.")
        else:
            user_guess = int(user_guess)
            self.tries_left -= 1
            self.try_label.config(text=f"Tries left: {self.tries_left}")

            if user_guess < self.random_number:
                self.result_label.config(text="Try higher.")
            elif user_guess > self.random_number:
                self.result_label.config(text="Try lower.")
            else:
                self.result_label.config(text="Congratulations! You guessed the number.")
                self.submit_button.config(state=DISABLED)
                self.restart_button.config(state=NORMAL)

            if self.tries_left == 0 and user_guess == self.random_number:
                self.result_label.config(text="Congratulations! You guessed the number.")
                self.submit_button.config(state=DISABLED)
                self.restart_button.config(state=NORMAL)
            elif self.tries_left == 0:
                self.result_label.config(text=f"Out of tries. The number was {self.random_number}.")
                self.submit_button.config(state=DISABLED)
                self.restart_button.config(state=NORMAL)

    def restart_game(self):
        self.random_number = ran.randint(1, 100)
        self.tries_left = 5
        self.try_label.config(text=f"Tries left: {self.tries_left}")
        self.result_label.config(text="")
        self.submit_button.config(state=NORMAL)
        self.restart_button.config(state=DISABLED)
        self.entry.delete(0, END)


def guess():
    def main():
        window = Tk()
        window.geometry('250x155')
        GuessTheNumber(window)

        def goback():
            window.withdraw()
            start.deiconify()

        Button(window, text="Back", command=goback).place(x=105, y=133)
        window.mainloop()

    if __name__ == "__main__":
        main()


def rps():
    root = Tk()
    root.geometry("300x300")
    root.title("Rock Paper Scissor Game")
    computer_value = {
        "0": "Rock",
        "1": "Paper",
        "2": "Scissor"
    }

    def reset_game():
        b1["state"] = "active"
        b2["state"] = "active"
        b3["state"] = "active"
        l1.config(text="Player        ")
        l3.config(text="Computer")
        l4.config(text="")

    # Disable the Button

    def button_disable():
        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    # If player selected rock

    def isrock():
        c_v = computer_value[str(ran.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Player Win"
        else:
            match_result = "Computer Win"
        l4.config(text=match_result)
        l1.config(text="Rock       ")
        l3.config(text=c_v)
        button_disable()

    # If player selected paper

    def ispaper():
        c_v = computer_value[str(ran.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Computer Win"
        else:
            match_result = "Player Win"
        l4.config(text=match_result)
        l1.config(text="Paper      ")
        l3.config(text=c_v)
        button_disable()

    # If player selected scissor

    def isscissor():
        c_v = computer_value[str(ran.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Computer Win"
        elif c_v == "Scissor":
            match_result = "Match Draw"
        else:
            match_result = "Player Win"
        l4.config(text=match_result)
        l1.config(text="Scissor        ")
        l3.config(text=c_v)
        button_disable()

    # Add Labels, Frames and Button
    Label(root,
          text="Rock Paper Scissor",
          font="normal 20 bold",
          fg="blue").pack(pady=20)

    frame = Frame(root)
    frame.pack()

    l1 = Label(frame,
               text="Player           ",
               font=10)

    l2 = Label(frame,
               text="VS           ",
               font="normal 10 bold")

    l3 = Label(frame, text="Computer", font=10)

    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack()

    l4 = Label(root,
               text="",
               font="normal 20 bold",
               bg="white",
               width=15,
               borderwidth=2,
               relief="solid")
    l4.pack(pady=20)

    frame1 = Frame(root)
    frame1.pack()

    b1 = Button(frame1, text="Rock",
                font=10, width=7,
                command=isrock)
    b1.pack(side=LEFT, padx=10)
    b2 = Button(frame1, text="Paper ",
                font=10, width=7,
                command=ispaper)
    b2.pack(side=LEFT, padx=10)
    b3 = Button(frame1, text="Scissor",
                font=10, width=7,
                command=isscissor)
    b3.pack(padx=10)
    Button(root, text="Play Again",
           font=10, fg="red",
           bg="black", command=reset_game).place(x=70, y=225)

    def goback():
        root.withdraw()
        start.deiconify()

    Button(root, text="Back", font=10, fg="red", bg="black", command=goback).place(x=175, y=225)

    root.mainloop()


def shapes():
    def draw_shape():
        length = float(length_entry.get())
        shape = shape_var.get()
        print("Shape Chosen: - ", shape)

        # Clear the canvas
        turtle.reset()

        if shape == "Circle":
            turtle.circle(length)
        elif shape == "Square":
            for i in range(4):
                turtle.forward(length)
                turtle.left(90)
        elif shape == "Triangle":
            for i in range(3):
                turtle.forward(length)
                turtle.left(120)

    def clear_canvas():
        turtle.reset()
        length_entry.delete(0, "end")

    # Initialize the tkinter window
    root = tk.Tk()
    root.title("Shape Drawer")

    # Create a frame for the inputs and buttons
    input_frame = ttk.LabelFrame(root, text="Shape Drawer (Selected shape shown in output window)")
    input_frame.grid(row=0, column=0, padx=10, pady=15, sticky="w")

    # Length input
    length_label = ttk.Label(input_frame, text="Length:")
    length_label.grid(row=0, column=0, padx=5)
    length_entry = ttk.Entry(input_frame)
    length_entry.grid(row=0, column=1, padx=5)

    # Shape selection
    shape_var = tk.StringVar()
    shape_var.set("Circle")
    shape_label = ttk.Label(input_frame, text="Select Shape:")
    shape_label.grid(row=1, column=0, padx=5)
    shape_option_menu = tk.OptionMenu(input_frame, shape_var, "Default - Circle", "Circle", "Square", "Triangle")
    shape_option_menu.grid(row=1, column=1, padx=5)

    # Draw button
    draw_button = ttk.Button(input_frame, text="Draw Shape", command=draw_shape)
    draw_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    # Clear button
    clear_button = ttk.Button(input_frame, text="Clear Canvas", command=clear_canvas)
    clear_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def goback():
        root.withdraw()
        start.deiconify()

    back_button = ttk.Button(input_frame, text="Back", command=goback)
    back_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
    # Initialize the Turtle graphics canvas
    canvas = turtle.ScrolledCanvas(root)
    canvas.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    turtle_screen = turtle.TurtleScreen(canvas)
    turtle_screen.bgcolor("white")

    root.mainloop()


start.geometry('1050x500')
start.title('JKJ MINI GAMES')
start.configure(background='green')
f = ("Times bold", 14)


def end():
    text_val1 = "Thank You for playing on JKJ Mini-Games"
    engine.getProperty("rate")
    engine.setProperty("rate", 180)
    engine.say(text_val1)
    engine.runAndWait()
    start.destroy()


def firstGame():
    start.withdraw()
    paint()


def secondGame():
    start.withdraw()
    guess()


def fourthGame():
    start.withdraw()
    rps()


def fifthGame():
    start.withdraw()
    shapes()


Label(start, text='WELCOME TO JKJ MINI-GAMES', fg="red", font=('bold', '10', 'underline')).place(x=450, y=30)
photo = PhotoImage(file=r"pic1.png")
photo_image = photo.subsample(3, 3)
Button(
    start,
    image=photo_image,
    text="Paint on a Canvas",
    compound=LEFT,
    font=f,
    fg="red",
    width=250,
    command=firstGame
).place(x=100, y=100)
photo1 = PhotoImage(file=r"pic2.png")
photo_image1 = photo1.subsample(3, 3)
Button(
    start,
    image=photo_image1,
    compound=LEFT,
    text="Guess the Number",
    font=f,
    fg="red",
    width=250,
    command=secondGame
).place(x=420, y=100)

photo3 = PhotoImage(file=r"fourthpic.png")
photo_image3 = photo3.subsample(3, 3)
Button(
    start,
    image=photo_image3,
    compound=LEFT,
    text="Rock,Paper,Scissors",
    font=f,
    fg="red",
    width=250,
    command=fourthGame
).place(x=730, y=100)
photo4 = PhotoImage(file=r"lgame.png")
photo_image4 = photo4.subsample(3, 3)
Button(
    start,
    image=photo_image4,
    compound=LEFT,
    text="Shape Maker",
    font=f,
    fg="red",
    width=250,
    command=fifthGame
).place(x=200, y=300)
photo5 = PhotoImage(file=r"end.png")
photo_image5 = photo5.subsample(3, 3)
Button(
    start,
    image=photo_image5,
    compound=LEFT,
    text="End Mini-games",
    font=f,
    fg="red",
    height=75,
    width=250,
    command=end
).place(x=600, y=300)
start.mainloop()
