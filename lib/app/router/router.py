from lib.modules.about import AboutPage
from lib.modules.contact import ContactPage
from lib.modules.home import HomePage
import customtkinter
from typing import List


class Router:
    def __init__(self, parent):
        self.parent = parent
        self.routes = {"home": HomePage, "contact": ContactPage, "about": AboutPage}
        self.frames = {}
        self.create_frames()

    def create_frames(self):
        for route, FrameClass in self.routes.items():
            frame = FrameClass(self.parent, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[route] = frame

    def show_frame(self, page_route):
        frame = self.frames[page_route]
        frame.tkraise()
