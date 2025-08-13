def format_name(full_name):
  """Formats a full name as 'Last, First'."""
  parts = full_name.split()
  if len(parts) >= 2:
    return f"{parts[-1]}, {' '.join(parts[:-1])}"
  else:
    return full_name # Handle cases with less than two parts

# Example usage:
print(format_name("John Doe"))
print(format_name("Jane M. Smith"))
print(format_name("Peter Jones"))