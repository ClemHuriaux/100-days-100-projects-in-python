# Exercises 1 and 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num**2 for num in numbers]

even_numbers = [num for num in numbers if num % 2 == 0]

# Exercise 3
with open("file1.txt") as f:
    list1 = f.read().splitlines()
with open("file2.txt") as f:
    list2 = f.read().splitlines()

result = [int(num) for num in list1 if num in list2]
print(result)
