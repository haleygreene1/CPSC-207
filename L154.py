class Fabric:
    def __init__(self,countryOfOrigin,color):
        self.countryOfOrigin= countryOfOrigin
        self.color = color

    def __str__(self):
        return self.countryOfOrigin + "("+ str(self.color)+")"

f1 = Fabric("Australia","Red")

print(f1)
