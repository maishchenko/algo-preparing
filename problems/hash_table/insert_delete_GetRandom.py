# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/


from random import randint

class RandomizedSet:

    def __init__(self):
        self._set: set[int] = set()
        self._positions: dict = {}
        self._count = 0
        

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        self._set.add(val)
        self._count += 1
        self._positions[self._count] = val
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self._set:
            return False
        self._set.remove(val)
        del self._positions[self._count]
        self._count -= 1
        return True
        
    def getRandom(self) -> int:
        if self._count == 0:
            return
        rand_idx = randint(1, self._count)
        return self._positions[rand_idx]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    rand_set = RandomizedSet()
    print(rand_set.insert(2)) # True
    print(rand_set.insert(3)) # True
    print(rand_set.insert(3)) # False
    print(rand_set.getRandom())
    
    print(rand_set.remove(3)) # True
    print(rand_set.getRandom()) # 2
    print(rand_set.remove(3)) # False
