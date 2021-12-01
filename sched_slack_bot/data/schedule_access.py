import abc
from typing import List

from sched_slack_bot.model.schedule import Schedule


class ScheduleAccess(abc.ABC):
    @abc.abstractmethod
    def get_available_schedules(self) -> List[Schedule]:
        raise NotImplemented()

    @abc.abstractmethod
    def save_schedule(self, schedule: Schedule) -> None:
        raise NotImplemented()

    @abc.abstractmethod
    def delete_schedule(self, schedule: Schedule) -> None:
        raise NotImplemented()
