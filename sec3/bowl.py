class Scoop():
    def __init__(self,flavor):
        self.flavor = flavor

class bowl():
    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *args):
        self.scoops += args

    def flavors(self):
        return [one_scoop.flavor for one_scoop in self.scoops]

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

b = bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b.flavors())