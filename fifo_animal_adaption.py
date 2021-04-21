class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, animal_type):
        if animal_type.lower() == "cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_cat(self):
        if len(self.cats) != 0:
            return self.cats.pop(0)
        else:
            return None

    def dequeue_dogs(self):
        if len(self.dogs) != 0:
            return self.dogs.pop(0)
        else:
            return None

    def return_any(self):
        if len(self.cats) == 0:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)

animal = AnimalShelter()
animal.enqueue('cat1','cAt')
animal.enqueue('cat2','cat')
animal.enqueue('cat3','CAT')
animal.enqueue('dog1','DOG')
animal.enqueue('dog2','dOG')
print(animal.dequeue_cat())
print(animal.dequeue_dogs())
print(animal.return_any())


