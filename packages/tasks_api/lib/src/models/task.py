from datetime import datetime
from packages.tasks_api.lib.src.models.base import Base
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    def __repr__(self) -> str:
        return f"Task(title={self.title}, description={self.description}, create_date={self.create_date})"
