class Scoop():
    def __init__(self,flavor):
        self.flavor = flavor

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)

scoops = [s1, s2, s3]

for one_scoop in scoops:
    print(one_scoop.flavor)