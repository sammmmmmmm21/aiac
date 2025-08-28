def sort_list(data):
    return sorted(data, key=str)

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
# Output: [1, 2, 3, 'apple', 'banana']
