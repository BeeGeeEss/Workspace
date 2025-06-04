class Plants():
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height 

class GreenPlants(Plants):
    def __init__(self, name, height, colour) -> None:
        super().__init__(name, height)
        self.colour = colour

class LandPlants(GreenPlants):
    def __init__(self, name, height, colour) -> None:
        super().__init__(name, height, colour)

class VascularPlants(LandPlants):
    def __init__(self, name, height, colour, rootLength) -> None:
        super().__init__(name, height, colour)
        self.rootLength = rootLength

class SeedPlants(VascularPlants):
    def __init__(self, name, height, colour, rootLength, pollinationMethod) -> None:
        super().__init__(name, height, colour, rootLength)
        self.pollinationMethod = pollinationMethod

class Gymnosperms(SeedPlants):
    def __init__(self, name, height, colour, rootLength, pollinationMethod, coneSize) -> None:
        super().__init__( name,height, colour, rootLength, pollinationMethod)
        self.coneSize = coneSize

class Angiosperms(SeedPlants):
    def __init__(self, name, height, colour, rootLength, pollinationMethod, flowerSize, petalCount, flowerColour) -> None:
        super().__init__(name, height, colour, rootLength, pollinationMethod)
        self.flowerSize = flowerSize
        self.petalCount = petalCount
        self.flowerColour = flowerColour

frangipani = Angiosperms("Frangipani", 200, "green and brown", 50, "Birds & bees", 5, 6, "White")
pineTree = Gymnosperms("Pine Tree", 1000, "green and brown", 100, "animals eating cones", 20)
wheat = SeedPlants("Wheat grass", 150, "yellow and green", 30, "wind")
fern = VascularPlants("Maidenhair Fern", 50, "green", 30)
algae = GreenPlants("Gross Algae", 1, "green and black")
mold = Plants("Weird green stuff", 1)

for plant in (frangipani, pineTree, wheat, fern, algae, mold):
    print (plant.name)
