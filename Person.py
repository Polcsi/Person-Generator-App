from Address import Address

class Person:
    FirstName: str
    LastName: str
    Gender: str
    Age: int
    address: Address
    
    address = Address()
    @property
    def FirstName(self):
        return self._FirstName
    @FirstName.setter
    def FirstName(self, firstname):
        self._FirstName = firstname
    @property
    def LastName(self):
        return self._LastName
    @LastName.setter
    def LastName(self, lastname):
        self._LastName = lastname
    @property
    def Gender(self):
        return self._Gender
    @Gender.setter
    def Gender(self, gender):
        self._Gender = gender
    @property
    def Age(self):
        return self._Age
    @Age.setter
    def Age(self, age):
        self._Age = age