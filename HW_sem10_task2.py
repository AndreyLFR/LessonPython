class LotteryGame:
    def __init__(self, ticket, result):
        self.ticket = ticket
        self.result = result

    def compare_list(self):
        result = list(set(self.ticket) & set(self.result))
        count = len(result)
        print(f'Совпадающие числа: {result}\n'
              f'Количество совпадающих чисел: {count}')

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
game = LotteryGame(list1, list2)
game.compare_list()