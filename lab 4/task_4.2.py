def count_vowels(s):
    """
    Counts the number of vowels in the input string.
    Handles both uppercase and lowercase vowels.
    """
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
examples = ["hello", "Python", "AEIOU"]
for word in examples:
    print(f"'{word}' has {count_vowels(word)} vowels.")
