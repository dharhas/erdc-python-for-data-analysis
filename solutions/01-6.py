def get_longest(a, b, reverse=False):
    if len(a) > len(b):
        longest, smallest = a, b
    else:
        longest, smallest = b, a

    if reverse:
        return smallest
    else:
        return longest


assert get_longest('hello', 'goodbye') == 'goodbye'
assert get_longest('hello', 'goodbye', reverse=True) == 'hello'