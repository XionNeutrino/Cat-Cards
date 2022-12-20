from tkinter import *
from tkinter import ttk


class Scene:
    def __init__(self):
        self.children: list[Scene]
        self.win = Tk()

    # adds a child scene
    def add_child(self, child):
        self.children.append(child)

    # draws each of the scene's children
    def draw(self):
        for child in self.children:
            child.draw()


class Sprite(Scene):
    def __init__(self, xpos, ypos, scale, img_path: str):
        self.xpos = xpos
        self.ypos = ypos
        self.scale = scale
        self.img_path = img_path

    def draw(self):
        super().draw()


def setup(scene: Scene):
    # title the window
    scene.win.title("Cat Cards")

    # begin the mainloop
    scene.win.mainloop()


def drag_handler(event):
    pass

    # determine which sprite the drag intercepted
    # enlarge that sprite while moving it to the cursor until the drag event stops
    # when event stops, deenglarge the sprite
