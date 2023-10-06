import math
class StudentWorkloadCalculator():
    def __init__(self, _classHours = 0, _workHours = 0):
        self._classHours = classHours
        self._workHours = workHours
    
    def getClassHours(self):
        return self._classHours
    
    def setClassHours(self, newClassHours = 0):
        self.classHours = newClassHours

    def getWorkHours(self):
        return self._workHours
    
    def setClassHours(self, newWorkHours = 0):
        self.classHours = newWorkHours

    def calculateWorkload(self):
        return 2 * self._classHours + self._workHours

classHours = int(input())
workHours = int(input())
user1 = StudentWorkloadCalculator(4, 5)
print(user1.getClassHours())
print(user1.getWorkHours())
print(user1.calculateWorkload())


 