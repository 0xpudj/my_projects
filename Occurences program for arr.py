def count_occurrences(arr, v):
    return arr.count(v)

def most_frequent_element(arr):
    frequency = {}
    for i in set(arr):
        frequency[i] = count_occurrences(arr, i)
    
    return max(frequency, key=frequency.get)

array = [3, 1, 3, 2, 1, 3, 2, 1, 1, 4]
v = int(input("Enter a number: "))
print(f"The value {v} occurences {count_occurrences(array, v)} times.\n")

print(f"Most frequent element: {most_frequent_element(array)}")
print(f"Occurrences: {count_occurrences(array, most_frequent_element(array))}")