class Balloon:

    def __init__(self, tagId : int, color : str) -> None:
        self.color = color
        self.tagId = tagId
        self.x = []
        self.y = []
        self.count = 1

    def addPosition(self, pos : tuple([float, float])):
        self.x.append(pos[0])
        self.y.append(pos[1])

    def getPosition(self) -> tuple([float, float]):
        avX = sum(self.x)/len(self.x)
        avY = sum(self.y)/len(self.y)
        self.count += 1
        return tuple([avX, avY])
    
    def equals(self, tagId, color) -> bool:
        return (self.color == color and self.tagId == tagId)