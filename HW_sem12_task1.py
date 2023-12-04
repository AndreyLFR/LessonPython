import csv


class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.path_file = subjects_file
        self.subjects_list = self.load_subjects(subjects_file)
        self.subjects = {}

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='') as csvfile:
            return list(csv.reader(csvfile, delimiter=','))[0]

    def __setattr__(self, key, value):
        if key == 'name' and (not value.istitle() or True in [i.isdigit() for i in value]):
            raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return object.__getattribute__(self, item)

    def add_grade(self, subject, grade):
        if not grade in range(2, 5 + 1) or not isinstance(grade, int):
            raise ValueError(f'Оценка должны быть целым числом от 2 до 5')
        elif not subject in self.subjects_list:
            raise ValueError(f'Недопустимое наименование предмета')
        else:
            if subject in self.subjects:
                if 'grade' in self.subjects[subject]:
                    list_value = self.subjects[subject]['grade']
                    list_value.append(grade)
                    self.subjects[subject]['grade'] = list_value
                else:
                    self.subjects[subject]['grade'] = [grade]
            else:
                self.subjects[subject] = {'grade': [grade]}


    def add_test_score(self, subject, test_score):
        if not test_score in range(0, 100 + 1) or not isinstance(test_score, int):
            raise ValueError(f'Результат теста должен быть целым чмслом от 0 до 100')
        elif not subject in self.subjects_list:
            raise ValueError(f'Недопустимое наименование предмета')
        else:
            if subject in self.subjects:
                if 'test_score' in self.subjects[subject]:
                    list_value = self.subjects[subject]['test_score']
                    list_value.append(test_score)
                    self.subjects[subject]['test_score'] = list_value
                else:
                    self.subjects[subject]['test_score'] = [test_score]
            else:
                self.subjects[subject] = {'test_score': [test_score]}

    def __str__(self):
        return f'Cтудент: {self.name}\n' \
               f'Предметы: {", ".join(self.subjects.keys())}'

    def get_average_test_score(self, subject):
        if not subject in self.subjects_list:
            raise ValueError(f'Недопустимое наименование предмета')
        elif not subject in self.subjects or not 'test_score' in self.subjects[subject]:
            raise ValueError(f'Тесты по предмету не проводились')
        else:
            return sum(self.subjects[subject]['test_score']) / len(self.subjects[subject]['test_score'])

    def get_average_grade(self):
        sum_ = 0
        count_ = 0
        for subj, value in self.subjects.items():
            if 'grade' in value:
                count_ = count_ + len(self.subjects[subj]['grade'])
                sum_ = sum_ + sum(self.subjects[subj]['grade'])
        return sum_ / count_

student = Student('Иван Иванович', 'subjects.csv')

student.add_grade('Математика', 4)
student.add_test_score('Математика', 85)

student.add_grade('История', 5)
student.add_test_score('Истори', 92)
print(student)

average_test_score = student.get_average_test_score('Математика')
print(average_test_score)

average_grade = student.get_average_grade()
print(average_grade)