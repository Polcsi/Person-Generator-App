from RandomPerson import *
        
personGenerator: RandomPerson = RandomPerson()
for i in range(0, 3, 1):
    person: Person = personGenerator.generatePerson()
    print("------------------------------")
    print("BASIC INFORMATION")
    print(f"Firstname: {person.FirstName}\n\r"
          f"Lastname: {person.LastName}\n\r"
          f"Gender: {person.Gender}\n\r"
          f"Age: {person.Age}")
    print(f"\n\rCONTACT INFORMATION")
    print(f"City: {person.address.City}\n\r"
          f"State: {person.address.State}\n\r"
          f"Street: {person.address.Street}\n\r"
          f"Zip: {person.address.Zip}")
