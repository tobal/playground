'''
4.2 Medium: Truthiness Evaluation & Short-Circuit Default

     * Goal: Implement resolve_first_truthy(*args: typing.Any, default: typing.Any = None) -> typing.Any.
     * Description: Return the first value from *args that evaluates to a truthy boolean context, or
       default if all are falsy. Do not convert the returned value to bool.
     * Key Takeaway: In Python, logical or returns the actual operand object that satisfied truthiness,
       not a boolean literal True or False. Falsy objects include None, 0, 0.0, "", [], {}, set().
     * Expected Behavior:
          + resolve_first_truthy("", [], 0, "hello", "world") -> "hello"
          + resolve_first_truthy(None, False, 0.0, default="fallback") -> "fallback"
'''
import typing

def resolve_first_truthy(*args: typing.Any, default: typing.Any = None) -> typing.Any:
    truthies = (x for x in args if x or False) # using generator instead
    return next(truthies, default)
