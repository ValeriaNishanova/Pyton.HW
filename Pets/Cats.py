class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

# Вывод всех котов, имеющихся на сайте
    def __str__(self):
        return(f"Имя {self.name}, пол {self.gender}, возраст {self.age}")
