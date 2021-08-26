class Address:
    Street: str
    City: str
    State: str
    Zip: int
    
    @property
    def Street(self):
        return self._Street
    @Street.setter
    def Street(self, street):
        self._Street = str(street)
    @property
    def City(self):
        return self._City
    @City.setter
    def City(self, city):
        self._City = str(city)
    @property
    def State(self):
        return self._State
    @State.setter
    def State(self, state):
        self._State = state
    @property
    def Zip(self):
        return self._Zip
    @Zip.setter
    def Zip(self, zip):
        self._Zip = zip