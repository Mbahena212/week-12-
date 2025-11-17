# # Objective:
# # Students will understand how to create, modify, and access elements in Python lists.

# # Topics Covered:
# # Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# # Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)

#Collection are used to store multiple items in a single variable 
#lists are ordered collection of items
#lists are mutable, meaning you can changer their content 
#Lists are created using sqaure brackets 
List_of_fruits = ["apple", "banana", "cherry", "date"]
print(List_of_fruits)
print(type(List_of_fruits))
print(List_of_fruits[0])
print(List_of_fruits[1])
print(List_of_fruits[1:3])

List_of_fruits.reverse()
print(List_of_fruits)
print(List_of_fruits[::-1])

List_of_fruits.extend("elderberry", "grape", "mango")
print(List_of_fruits)
List_of_fruits.reverse()
print(List_of_fruits)


popped_item = List_of_fruits.pop()
print(popped_item)
print(List_of_fruits)
# # Practice Problems:
List_of_fruits.remove("banana")
List_of_fruits.insert(3, "banana")
List_of_fruits.sort()
print(List_of_fruits)

listofitems = list(range(1, 1001))
print(listofitems)
print(len(listofitems))
listofitems.extend(range(1001, 3000))
# # Create a list with 5 of your favorite foods.

# # Print the second and last item.

# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.