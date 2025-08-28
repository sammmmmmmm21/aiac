def sort_list(data):
	# Convert all elements to strings for consistent sorting
	return sorted(map(str, data))

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
