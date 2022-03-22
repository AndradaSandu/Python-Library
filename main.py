# def maximum(nums):
#     Max = 0
#     for item in nums:
#         if item > Max:
#             Max = item
#     return Max
#
#
# List = [2, 7, 8, 9, 12, 14, 56, 7, 2]
# print(maximum(List))




# def count(nums):
#     counter = 0
#     for el in nums:
#         if el == 1:
#             counter = counter + 1
#     return counter
#
# lst = [1, 3, 1, 1, 4, 5, 1, 1, 1, 5]
# print(count(lst))



# Function for nth fibonacci
# number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#
#     elif n == 0:
#         return 0
#
#     elif n == 1:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
# print(fibonacci(9))


# n = int(input("Enter the number for the factorial number?"))
# fact = 1
#
# for i in range(1, n+1):
#     print("i", i)
#     fact = fact * i
#
# print (f"The factorial of {n} is : ", end="")
# print (fact)
#



def sort(my_list):
    for el in range(len(my_list)):
        for item in range(len(my_list)):
            if my_list[el] < my_list[item]:
                temp = my_list[el]
                my_list[el] = my_list[item]
                my_list[item] = temp
my_list = [2,45,34,7,8,5,1,2,3,4,6,6,6,6,6,1000,-2]
sort(my_list)
print(my_list)
