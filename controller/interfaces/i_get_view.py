from abc import ABC, abstractmethod
from typing import List

from model.core.student import Student


class iGetView(ABC):

    @abstractmethod
    def printAllStudent(self, students: List['Student']) -> None:
        pass

    @abstractmethod
    def prompt(self, msg: str) -> str:
        pass

    @abstractmethod
    def printAllStudentEng(self, students: List['Student']) -> None: # МЕТОД ДЛЯ ViewClassEng
        pass
    @abstractmethod
    def promptForStudentId(self) -> int:
        pass