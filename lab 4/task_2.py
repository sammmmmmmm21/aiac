def centimeters_to_inches(cm):
    """
    Converts centimeters to inches using the correct conversion factor.
    1 inch = 2.54 centimeters
    """
    inches = cm / 2.54
    return inches

# Example usage
centimeters = float(input("Enter length in centimeters: "))
inches = centimeters_to_inches(centimeters)
print(f"{centimeters} cm is equal to {inches:.3f} inches.")
