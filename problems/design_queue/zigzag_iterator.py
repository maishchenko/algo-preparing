# 281. Zigzag Iterator (subscribe)
# https://leetcode.com/problems/zigzag-iterator/description/
#
# Нужно реализовать итератор который принимает два списка и возвращает их элементы в шахматном порядке — поочерёдно из первого и второго списка. 
# Когда один список заканчивается — продолжаем возвращать элементы из оставшегося.
# Три метода:
# ZigzagIterator(v1, v2) — инициализация с двумя списками
# hasNext() → True если ещё есть элементы, False если оба списка исчерпаны
# next() → возвращает следующий элемент в зигзаг-порядке

# Пример:
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]

# next() → 1   (из v1)
# next() → 3   (из v2)
# next() → 2   (из v1)
# next() → 4   (из v2)
# next() → 5   (из v2, v1 закончился)
# next() → 6   (из v2)
# hasNext() → False

# Входные данные: два списка целых чисел v1 и v2
# Результат: последовательность вызовов next() возвращает элементы в зигзаг-порядке

class Zigzagiterator:
    def __init__(self, list1: list[int], list2: list[int]):
        self.list1 = list1
        self.list2 = list2
        self.i = 0   # указатель на v1
        self.j = 0   # указатель на v2
        self.turn = 0  # 0 = очередь list1, 1 = очередь list2
        
    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        if self.i < len(self.list1) and self.j < len(self.list2):
            if not self.turn: # list1
                self.i += 1
                self.turn = 1
                return self.list1[self.i-1]
            else:
                self.j += 1
                self.turn = 0
                return self.list2[self.j-1]
        if self.i < len(self.list1):
            self.i += 1
            return self.list1[self.i-1]
        if self.j < len(self.list2):
            self.j += 1
            return self.list2[self.j-1]
        
    def hasNext(self) -> bool:
        if self.i < len(self.list1) or self.j < len(self.list2):
            return True
        return False
    

if __name__ == "__main__":
    zizag = Zigzagiterator(
        list1 = [1, 2],
        list2 = [3, 4, 5, 6]
    )
    print(zizag.next()) # 1
    print(zizag.next()) # 3
    print(zizag.next()) # 2
    print(zizag.next()) # 4
    print(zizag.next()) # 5
    print(zizag.next()) # 6
    print(zizag.next()) # StopIteration
