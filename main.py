from lib.app import App
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from packages.database_tasks_api.lib import DatabaseTasksApi
from packages.tasks_repository.lib import TasksRepository
from packages.tasks_api.lib import Task, Base


def main():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    taskApi = DatabaseTasksApi(Session=Session)
    tasksRepository = TasksRepository(taskApi=taskApi)
    task = Task(title="hello", description="hola")
    tasksRepository.addTask(task=task)
    tasks = tasksRepository.getTasks()
    if tasks:
        task = tasks[0]
        tasksRepository.deleteTask(task_id=task.id)
    app = App(tasksRepository=tasksRepository)
    app.router.show_frame("home")
    app.mainloop()


if __name__ == "__main__":
    main()
