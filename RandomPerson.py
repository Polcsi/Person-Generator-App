import random
from Person import *

class RandomPerson:
    firstNamesFemale = ["Alexandra", "Alison",
        "Maria", "Sophie","Wanda"]
    firstNamesMale = [
        "Brandon", "David", "Gordon", "Jonathan",
        "Peter"]
    lastNames = ["Abraham", "Campbell", "Ellison",
        "Henderson", "Johnston"]
    streets = ["2708 Adonais Way", "4154 Cherry Tree Drive",
        "3466 Wilmar FarmRoad", "1949 Jadewood Drive",
        "501 Blane Street"]
    cities = ["Atlanta", "Jacksonville", "Lanham",
        "Wheatfield", "Fairview Heights"]
    states = ["Georgia(GA)", "Florida(FL)",
        "Maryland(MD)", "Indiana(IN)", "Missouri(MO)"]
    
    def generateElementof(self, strArray: list) -> str:
        count: int = 0
        for i in strArray:
            count = count + 1    
        return strArray[random.randint(0, count-1)]
    
    def generateZip(self) -> int:
        return random.randint(1, 10000)
    
    def generateAge(self) -> int:
        return random.randint(18, 60)
    
    @staticmethod
    def generateGender() -> str:
        return "Female" if random.randint(0, 1) == 0 else "Male"
    
    def generatePerson(self) -> Person:
        person: Person = Person()
        personGenerator = RandomPerson()
        person.Gender = personGenerator.generateGender()
        person.FirstName = personGenerator.generateElementof(personGenerator.firstNamesFemale if person.Gender == "Female" else personGenerator.firstNamesMale)
        person.LastName = personGenerator.generateElementof(personGenerator.lastNames)
        person.Age = personGenerator.generateAge()
        person.address.Street = personGenerator.generateElementof(personGenerator.streets)
        person.address.City = personGenerator.generateElementof(personGenerator.cities)
        person.address.State = personGenerator.generateElementof(personGenerator.states)
        person.address.Zip = personGenerator.generateZip()
        return person