from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.CREAM_COLOUR = "#FEFBEA"
        self.FONT_NAME = "Times New Roman"
        self.COURSE_LINK = "https://skeleton973213.github.io/ting-site/"
        self.COURSE_TITLE = "Defence Against the Dark Arts"
        self.COURSE_DATE = "Sun"
        self.COURSE_TIME = "00.00-00.00"
        self.PLATFORM = "Zoomba"

    def show_link(self):
        messagebox.showinfo("Here's the link", self.COURSE_LINK)

    def setup(self):
        window = Tk()
        window.title("Today's schedule")
        canvas = Canvas(width=1440, height=810)
        background_img = PhotoImage(width=1440, height=810, file="background.png")
        background = canvas.create_image(720, 405, image=background_img)
        course_title = canvas.create_text(720, 350, text=self.COURSE_TITLE, fill=self.CREAM_COLOUR, font=(self.FONT_NAME, 60, "normal"))
        course_date = canvas.create_text(432, 200, text=self.COURSE_DATE, fill=self.CREAM_COLOUR, font=(self.FONT_NAME, 30, "normal"))
        course_time = canvas.create_text(1008, 200, text=self.COURSE_TIME, fill=self.CREAM_COLOUR, font=(self.FONT_NAME, 30, "normal"))
        course_platform = canvas.create_text(720, 500, text= self.PLATFORM, fill=self.CREAM_COLOUR, font=(self.FONT_NAME, 35, "normal"))
        button1 = Button(window, text="Get Link!", command=self.show_link, bg="#FFFDD0")
        button1_canvas = canvas.create_window(690, 600, anchor="nw", window=button1)
        canvas.pack()
        window.mainloop()

