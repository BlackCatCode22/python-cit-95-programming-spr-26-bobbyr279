class PartyAnimal:
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

# assign party animal class object to point at variable named s and j and give them a name
s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")

j.party()
s.party()
