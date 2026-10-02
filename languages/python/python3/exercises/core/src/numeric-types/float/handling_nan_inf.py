'''
2.2 Medium: Handling NaN and Infinities

     * Goal: Implement clean_float_array(values: list[float], fallback: float = 0.0) -> list[float].
     * Description: Process a list of floats, replacing all NaN, +inf, and -inf values with fallback,
       without importing the math module.
     * Key Takeaway: NaN has the unique property that x != x is True. Infinities satisfy abs(x) ==
       float('inf'). Operations on NaN propagate silently, causing subtle calculation bugs.
     * Expected Behavior:
          + clean_float_array([1.0, float('nan'), float('inf'), -float('inf'), 3.5], fallback=-1.0) ->
            [1.0, -1.0, -1.0, -1.0, 3.5]
'''

def clean_float_array(values: list[float], fallback: float = 0.0) -> list[float]:
    return [ fallback
            if (fl != fl or abs(fl) == float('inf'))
            else fl
            for fl in values ]
