class Archive:
    text_list = []
    number_list = []

    def __new__(cls, text, number):
        if not text in cls.text_list:
            instance = super().__new__(cls)
            instance.archive_text = text
            instance.archive_number = number
            cls.text_list.append(text)
            cls.number_list.append(number)
            return instance

    def __init__(self, text, number):
        try:
            self.archive_text = (text + text[0])[:-1]
        except (TypeError, IndexError):
            raise f'InvalidTextError'
        try:
            self.archive_number = float(number) if str(number).replace('.', '').isdigit() else float(' ')
        except ValueError:
            raise f'InvalidNumberError'

    def __str__(self):
        return f'Text is {self.archive_text} and number {self.archive_number}. Also {self.text_list} and {self.number_list}'


archive1 = Archive('', -42)
print(archive1)
archive2 = Archive('Запись 2', -3.14)
archive3 = Archive('Запись 3', 54)

print(archive2)