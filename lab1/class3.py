class Person:
    def __init__(self,person_id):
        self.person_id = person_id
        self.name = ""
        self.surname = ""
    
    def __str__(self):
        retval = "person with id " + str(self.person_id) 
        if self.name:
            retval += "\nName:" + self.name
        if self.surname:
            retval += "\nSurname:" + self.surname
        retval += "\nMother: " + self.mother.getFullName()
        retval += "\nFather: " + self.father.getFullName()
        return retval

    def setName(self,name):
        self.name = name

    def setSurname(self,surname):
        self.surname = surname

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getFullName(self):
        return self.name + " " + self.surname    

    def setMother(self, mother):
        self.mother = mother

    def setFather(self,father):
        self.father = father

    def setFriends(self,friends):
        self.friends = friends  




person1 = Person(1234)
person1.setName("Özen")
person1.setSurname("Beskan")


person2 = Person(7777)
person2.setName("Fatih")
person2.setSurname("Beskan")


person3 = Person(6678)
person3.setName("esra")
person3.setSurname("Beskan")
person3.setMother(person1)
person3.setFather(person2)
print(person3)