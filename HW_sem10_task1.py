class Animal:
    def __init__(self, args):
        self.name = args[0]

class Bird(Animal):
    def __init__(self, args):
        super().__init__(args)
        self.wingspan = args[1]

    def wing_length(self):
        return self.wingspan / 2

class Fish(Animal):
    def __init__(self, args):
        super().__init__(args)
        self.max_depth = args[1]

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        else:
            return 'Средневодная рыба'

class Mammal(Animal):
    def __init__(self, args):
        super().__init__(args)
        self.weight = args[1]

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(args)
        elif animal_type == 'Fish':
            return Fish(args)
        elif animal_type == 'Mammal':
            return Mammal(args)


animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())