import math


class ThirtySecondsFormatter:
    def __init__(self, fraction=32):
        # set to 32 by default, but can be changes
        self.fraction = fraction

    def convert(self, n: float) ->str:
        """
        returns thirtysecondsformatter of double
        """
        if not ((isinstance(n, int)) or (isinstance(n, float))):
            # check for incorrect type
            return "invalid type"
        # final str
        final = ''
        n_float = float(n) # if float is int, change to float
        if n_float < 0: # if the float is negative, change it to abs.
            n_float = abs(n_float)
            final += '-'
        split = math.modf(n_float) # split by decimal
        dollar = str(int(split[1]))
        thirtyseconds = str(round(split[0]*float(32), 2)) # convert to 32s and change to str
        thirtyseconds_cleaned = thirtyseconds.split('.')[0] # slice result
        if len(dollar) == 1:
            final += '0' + dollar + '-'
        else:
            final += dollar + '-'
        if len(thirtyseconds_cleaned) == 1:
            final += '0' + thirtyseconds_cleaned
        else:
            final += thirtyseconds_cleaned
        return final

