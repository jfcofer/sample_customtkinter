from packages.tasks_api.lib import TaskApi, Task


class TasksRepository:
    def __init__(self, taskApi: TaskApi) -> None:
        self.taskApi = taskApi

    def getTasks(self) -> list[Task]:
        return self.taskApi.getTasks()

    def addTask(self, *, task: Task) -> None:
        return self.taskApi.addTask(task=task)

    def deleteTask(self, *, task_id: int) -> None:
        return self.taskApi.deleteTask(task_id=task_id)
