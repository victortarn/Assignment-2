"""Contains three functions one that can return the factorial of an
integer, take a number and length to return a list of multiples
and return the largest number of a list.

Authour: Victor Tarnovski
Date 2020-10-14

"""


def cal_factorial(integer):
    """Takes a postive integer and returns the factorial"""
    x = integer - 1 #Number of times the integer is multiplied
    if integer == 0:
        return 1
    elif integer > 0:
        i = 0
        while i < x:
            i += 1
            integer *= i
        return integer


def list_multiples(number, length):
    """Takes a non-negative integer “number” and a positive integer “length”,
    and returns a list of multiples of “number” up to “length”"""
    b = number * length + 1 #Value at which the list ends
    list = [*range(number, b, number)]
    return list


def find_max(a_list):
    """Takes a list of integers "a_list" and returns the largest number"""
    i = 0
    max = a_list[i]
    length = len(a_list)
    
    while i < length:
        if a_list[i] > max:
            max = a_list[i]
        i += 1
    return max


if __name__ == "__main__":
    # Module Testing

    # Function cal_factorial(integer)

    # Case 1
    integer = 0
    print("The integer is", integer)
    factorial = cal_factorial(integer)
    print("The factorial is", factorial)
    print("\n")

    # Case 2
    integer = 32
    print("The integer is", integer)
    factorial = cal_factorial(integer)
    print("The factorial is", factorial)
    print("\n")
    
    # Case 3
    integer = 1
    print("The integer is", integer)
    factorial = cal_factorial(integer)
    print("The factorial is", factorial)
    print("\n")
    
    # Case 4
    integer = 5
    print("The integer is", integer)
    factorial = cal_factorial(integer)
    print("The factorial is", factorial)
    print("\n")
    
    # Case 5
    integer = 4
    print("The integer is", integer)
    factorial = cal_factorial(integer)
    print("The factorial is", factorial)
    print("\n")

    # Function list_multiples(number, length)

    #Case 1
    number = 1
    length = 1
    print("The number and length is", number, length)
    final_list = list_multiples(number, length)
    print("The final list is", final_list)
    print("\n")

    #Case 2
    number = 5
    length = 10
    print("The number and length is", number, length)
    final_list = list_multiples(number, length)
    print("The final list is", final_list)
    print("\n")

    #Case 3
    number = 10
    length = 5
    print("The number and length is", number, length)
    final_list = list_multiples(number, length)
    print("The final list is", final_list)
    print("\n")

    #Case 4
    number = 5
    length = 5
    print("The number and length is", number, length)
    final_list = list_multiples(number, length)
    print("The final list is", final_list)
    print("\n")

    #Case 5
    number = 2
    length = 100
    print("The number and length is", number, length)
    final_list = list_multiples(number, length)
    print("The final list is", final_list)
    print("\n")
    
    # Function find_max(a_list)

    #Case 1
    a_list = [1]
    print("The list is", a_list)
    max_value = find_max(a_list)
    print("The maximum value is", max_value)
    print("\n")

    #Case 2
    a_list = [1,2,3]
    print("The list is", a_list)
    max_value = find_max(a_list)
    print("The maximum value is", max_value)
    print("\n")

    #Case 3
    a_list = [1,2,3,4,5]
    print("The list is", a_list)
    max_value = find_max(a_list)
    print("The maximum value is", max_value)
    print("\n")

    #Case 4
    a_list = [5,4,3]
    print("The list is", a_list)
    max_value = find_max(a_list)
    print("The maximum value is", max_value)
    print("\n")

    #Case 5
    a_list = [10,45,34,456]
    print("The list is", a_list)
    max_value = find_max(a_list)
    print("The maximum value is", max_value)
    print("\n")
