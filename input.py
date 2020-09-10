from tkinter import *

size = 15
limit = int(600 / size) - 3  # Will be called in input


class Input:
    def __init__(self):

        self.root = Tk()
        self.root.title("Settings")
        self.root.configure(background='light blue')
        self.width_of_text = 50
        self.width_of_text_2 = 4
        # ENTRIES
        self.x1_input = Entry(self.root, width=self.width_of_text)
        self.y1_input = Entry(self.root, width=self.width_of_text)
        self.x2_input = Entry(self.root, width=self.width_of_text)
        self.y2_input = Entry(self.root, width=self.width_of_text)
        # TEXTS
        self.text = Text(self.root, height=4, width=40)
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
        self.text.insert(INSERT, "Please enter the coordinates \nof the starting pixel and the goal pixelbellow and "
                                 "press Next")
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
                print(" COORDINATES MUST BE AT LEAST 0")
            elif self.x1 > limit or self.x2 > limit or self.y1 > limit or self.y2 > limit:
                print(" COORDINATES'S LIMIT IS ", str(limit))
            elif self.x1 == self.x2 and self.y1 == self.y2:
                print("START AND TARGET CAN NOT BE THE SAME")
            else:
                self.root.destroy()
        except:
            print("Please enter an integer")

    def Button(self):
        # command take a function without ()
        button = Button(self.root, text="Submit", command=self.get_values)
        button.grid(row=5, column=1)

    def run(self):
        self.Entries()
        self.Button()
        self.Texts()
        self.root.mainloop()
