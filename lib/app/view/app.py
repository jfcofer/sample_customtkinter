import customtkinter
from packages.tasks_repository.lib import TasksRepository
from lib.app.router import Router

class App(customtkinter.CTk):

    def __init__(self, *, tasksRepository: TasksRepository):
        super().__init__()
        self.tasksRepository = tasksRepository
        self.build()

    def build(self):
        self.title("Tkinter Routing Example")
        self.geometry("400x300")
        
        self.router = Router(self)
