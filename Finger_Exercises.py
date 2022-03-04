def sumDigits(s):
    """
    Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5
    """
    try:
        sum_of_nums = sum([int(c) for c in s if c.isdigit()])
        print(sum_of_nums)
    except (TypeError, ValueError):
        print("Input must be a string")

def findAnEven(L):
    """
    Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number.
    """
    try:
        for i in L:
            if not i%2:
                return i
    except:
        raise ValueError("input does not include an even number")
    raise ValueError("input does not include an even number")

print(findAnEven([1, 5]))