from tkinter import *
from tkinter import messagebox


def warning_screen(message):
    window = Tk()
    window.withdraw()
    messagebox.showerror("Error", message)


class Input:
    def __init__(self, size):
        self.limit = int(600 / size) - 3
        self.root = Tk()
        self.root.title("Set Coordinates")
        self.root.configure(background='black')
        self.width_of_text = 40
        self.width_of_text_2 = 4
        # ENTRIES
        self.x1_input = Entry(self.root, width=self.width_of_text)
        self.y1_input = Entry(self.root, width=self.width_of_text)
        self.x2_input = Entry(self.root, width=self.width_of_text)
        self.y2_input = Entry(self.root, width=self.width_of_text)
        # TEXTS
        self.text = Text(self.root, height=4, width=30)
        self.text_1 = Text(self.root, height=1, width=self.width_of_text_2)
        self.text_2 = Text(self.root, height=1, width=self.width_of_text_2)
        self.text_3 = Text(self.root, height=1, width=self.width_of_text_2)
        self.text_4 = Text(self.root, height=1, width=self.width_of_text_2)
        # COORDINATES
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def Entries(self):
        self.x1_input.grid(row=1, column=1)
        self.y1_input.grid(row=2, column=1)
        self.x2_input.grid(row=3, column=1)
        self.y2_input.grid(row=4, column=1)

    def Texts(self):
        self.text.insert(INSERT, "Enter the coordinates \nof the starting pixel and the goal pixel bellow and "
                                 "press \nNext")
        self.text.grid(row=0, column=1)
        self.text_1.insert(INSERT, "X1")
        self.text_1.grid(row=1, column=0)
        self.text_2.insert(INSERT, "Y1")
        self.text_2.grid(row=2, column=0)
        self.text_3.insert(INSERT, "X2")
        self.text_3.grid(row=3, column=0)
        self.text_4.insert(INSERT, "Y2")
        self.text_4.grid(row=4, column=0)

    def get_values(self):
        try:
            self.x1 = int(self.x1_input.get())
            self.y1 = int(self.y1_input.get())
            self.x2 = int(self.x2_input.get())
            self.y2 = int(self.y2_input.get())
            if self.x1 < 0 or self.x2 < 0 or self.y1 < 0 or self.y2 < 0:
                warning_screen("Coordinates can not be negative")
            elif self.x1 > self.limit or self.x2 > self.limit or self.y1 > self.limit or self.y2 > self.limit:
                limit_msg = "Coordinate's limit is " + str(self.limit)
                warning_screen(limit_msg)
            elif self.x1 == self.x2 and self.y1 == self.y2:
                warning_screen("Start can not be equal to target")
            else:
                self.root.quit()
                self.root.destroy()
        except:
            warning_screen("Please enter an integer")

    def Button(self):
        button = Button(self.root, text="SUBMIT", command=self.get_values)
        Button(self.root, text="Quit", command=self.root.quit())
        button.grid(row=5, column=1)

    def run(self):
        self.Entries()
        self.Button()
        self.Texts()
        self.root.mainloop()
