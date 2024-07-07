from packages.tasks_api.lib.src.models.task import Task
from typing import List
from abc import ABC, abstractmethod


class TaskApi(ABC):
    @abstractmethod
    def getTasks(self) -> List[Task]:
        pass

    @abstractmethod
    def addTask(self, *, task: Task) -> None:
        pass

    @abstractmethod
    def deleteTask(self, *, task_id: int) -> None:
        pass
