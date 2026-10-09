'''
4.3 Hard: Custom Object Truthiness Control (__bool__ vs __len__)

     * Goal: Implement a class SmartBuffer that encapsulates a dynamic list of items, with configurable
       boolean evaluation rules.
     * Description:
          + If instantiated with eval_mode="count", bool(buffer) returns True if and only if len(buffer) >
            0.
          + If instantiated with eval_mode="sum", bool(buffer) returns True if and only if sum(elements)
            != 0.
     * Key Takeaway: When Python evaluates bool(obj), it first looks for __bool__(). If __bool__() is not
       defined, it falls back to __len__() != 0. If neither is defined, instances of user-defined classes
       are always True.
     * Expected Behavior:
          + buf = SmartBuffer([-5, 5], eval_mode="sum") -> len(buf) == 2, but bool(buf) == False.
          + buf2 = SmartBuffer([-5, 5], eval_mode="count") -> bool(buf2) == True.
'''

class SmartBuffer(list):
    def __init__(self, buffer: list, eval_mode: str):
        super().__init__(buffer)
        self.eval_mode = eval_mode

    def __bool__(self):
        if self.eval_mode == "sum":
            return sum(self) != 0
        elif self.eval_mode == "count":
            return len(self) > 0
