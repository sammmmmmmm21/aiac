def count_lines_in_file(filename):
    """
    Reads a .txt file and returns the number of lines.
    Assumes the file exists and is readable.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = "example.txt"
line_count = count_lines_in_file(file_path)
if line_count is not None:
    print(f"The file '{file_path}' has {line_count} lines.")
