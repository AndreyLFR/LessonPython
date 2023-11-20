from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls)
        instance.author = author
        instance.value = value
        instance.t = datetime.now().strftime("%Y-%m-%d %H:%M")
        return instance

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.t})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"

event = MyStr('Завершилось тестирование', 'John')
print(event)

my_string =MyStr('Пример текста', 'Иван')
print(my_string)

my_string = MyStr('Мама мыла раму', 'Маршак')
print(repr(my_string))