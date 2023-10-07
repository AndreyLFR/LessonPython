names = ['Alice', 'Bob', 'Charlie']
salary = [5000, 6000, 7000]
bonus = ['10%', '5%', '15%']

print({names[i]: salary[i] * float(bonus[i].replace('%', '')) / 100 for i in range(min(len(names), len(salary), len(bonus)))})