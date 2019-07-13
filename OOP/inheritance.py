class Pet:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed


class Dog(Pet):
    def __init__(self,name, breed):
        super().__init__(name, breed)



thePet = Pet("PET","all")
danny = Dog("Danny","GSD")

print("Is danny a Pet:", str(isinstance(danny, Pet)))
print("Is danny a dog:",str(isinstance(danny, Dog)))

