from typing import List, Dict
from model.core.student import Student
from controller.interfaces.i_get_model import iGetModel

class ModelClassHash(iGetModel): # используем Dict вместо HashMap 
    def __init__(self, initial_data: Dict[int, Student] = None):
        self.students_hash = {} if initial_data is None else initial_data

    def getStudents(self) -> List[Student]:
        return list(self.students_hash.values())

    def addStudent(self, student: Student) -> None:
        self.students_hash[student.id] = student

    def removeStudent(self, student_id: int) -> None: # добавляем функцию remove 
        if student_id in self.students_hash:
            del self.students_hash[student_id]