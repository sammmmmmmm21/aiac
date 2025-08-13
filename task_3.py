def format_name(full_name):
    """
    Formats a full name from 'First Last' to 'Last, First'.
    Assumes the input contains exactly two parts: first and last name.
    """
    parts = full_name.strip().split()
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two words: first and last name.")
    
    first, last = parts
    return f"{last}, {first}"

# Example usage
names = ["John Doe", "Alice Johnson", "Michael Smith"]
for name in names:
    print(format_name(name))
