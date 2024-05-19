"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array."""
    for item in items:
        print(item)
# output_all_items([1, 'hello', True])

def get_all_evens(nums):
    """Given a list of numbers, return a list of all even numbers."""
    return [num for num in nums if num % 2 == 0]
# print(get_all_evens([7, 8, 10, 1, 2, 2]))


def get_odd_indices(items):
    """Given a list of numbers, return a list of all odd numbers."""
    #return [item for item in items if item % 2 != 0]
    odd_indices = []
    for item, index in enumerate(items):
        if item % 2 != 0:
            odd_indices.append(index)
    return odd_indices
# print(get_odd_indices([1, 'hello', True, 500]))


def print_as_numbered_list(items):
    """Given a list, output a numbered list."""
    i = 1

    for item in items:
        print(f"{i} {item}")
        i += 1
# print(print_as_numbered_list([1, 'hello', True]))

def get_range(start, stop):
    """Return a list of numbers in a certain range."""
    return [num for num in range(start, stop)]
# print(get_range(0, 5))
# print(get_range(1, 3))

def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'."""
    chars = []

    for letter in word:
        if letter in "AEIOUaeiou":
            chars.append("*")
        else:
            chars.append(letter)
    return " ".join(chars)
print(censor_vowels('hello world'))

def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case."""

    return "_".join().upper()
print(snake_to_camel('hello_world'))

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
