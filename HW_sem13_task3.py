class InvalidNameError:

    def __str__(self, name):
        self.name = name

    def __str__(self):
        return f'InvalidNameError{self.name}'


class InvalidAgeError:

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'InvalidAgeError{self.age}'


class InvalidIdError:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'InvalidIDError {self.id}'

class Person:

    def __init__(self, last_name: str, name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            raise InvalidNameError
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise InvalidNameError
        if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            raise InvalidNameError
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError
        self.last_name = last_name
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def birthday(self):
        self.age += 1

class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, last_name: str, name: str, patronymic: str, age: int, id: int):
        super().__init__(last_name, name, patronymic, age)
        if not 100000 <= id < 1000000 or not isinstance(id, int):
            return InvalidIdError
        self.id = id

    def __str__(self):
        return f'{self.id}, {self.name}'

    def get_level(self):
        return sum([int(i) for i in str(id)]) % 7

emp1 = Employee(last_name='ggg', name='John', patronymic='Doe', age=29, id=111111)
print(emp1)