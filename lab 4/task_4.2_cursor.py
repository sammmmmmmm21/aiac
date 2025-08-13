def count_vowels(text):
  """Counts the number of vowels in a string."""
  vowels = "aeiouAEIOU"
  count = 0
  for char in text:
    if char in vowels:
      count += 1
  return count

# Example usage:
print(count_vowels("hello"))
print(count_vowels("AEIOU"))
print(count_vowels("Rythm"))
print(count_vowels("This is a test string."))