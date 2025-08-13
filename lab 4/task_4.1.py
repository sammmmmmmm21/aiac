def count_vowels(s):
    """
    Counts the number of vowels in the input string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
