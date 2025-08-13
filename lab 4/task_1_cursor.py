def is_leap(year):
  """Checks if a given year is a leap year."""
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage:
year_to_check = 2024
if is_leap(year_to_check):
  print(f"{year_to_check} is a leap year.")
else:
  print(f"{year_to_check} is not a leap year.")