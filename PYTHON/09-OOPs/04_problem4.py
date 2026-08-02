class Animal:
    pass


class Pet(Animal):
    def dog(self):
        self.dog_name = "Dog"
    def cat(self):
        self.catname = "cat"


class dog(Pet):
    def Dog(self):
        super().dog()
        print(f" {self.dog_name} barks,bow bow")

class cat(Pet):
    def Cat(self):
        super().cat()
        print(f"{self.catname} meows,meow meow")


# Example usage:
my_pet = dog()
my_pet2 = cat()
my_pet.Dog()
my_pet2.Cat()