from typing import List
from packages.tasks_api.lib import TaskApi, Task
from sqlalchemy.orm import sessionmaker


class DatabaseTasksApi(TaskApi):
    def __init__(self, *, Session: sessionmaker):
        super().__init__()
        self.Session = Session

    def getTasks(self) -> List[Task]:
        with self.Session() as session:
            return session.query(Task).all()

    def deleteTask(self, *, task_id: int) -> None:
        with self.Session.begin() as session:
            try:
                task = session.query(Task).filter(Task.id == task_id).one()
                session.delete(task)
                print("Taks deleted successfully: : {task}")
            except Exception as e:
                print("Failed to delete task:", str(e))

    def addTask(self, *, task: Task) -> None:
        with self.Session.begin() as session:
            session.add(task)
            print(f"Task saved succesfully: {task}")
