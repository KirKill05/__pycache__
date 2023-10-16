class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name 
        self.__age  = age
        self.__weight = weight
        self.__height = height
    
    def getBMI(self):
        bmi = self.__weight  / (self.__height * self.__height)
        return round(bmi * 100) / 100 

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight 

    def getHeight(self):
        return self.__height

person1 = BMI("Alva", 20, 60, 1.8)
print(person1.getBMI())
print(person1.getStatus())