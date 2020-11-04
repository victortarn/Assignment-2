"""Program that can print the factorial of an integer,
take a number and length to print a list of multiples
and print the largest number of a list.

Authour: Victor Tarnovski
Date 2020-10-14

"""

import fun_math


def main():
    print("""Please choose your task:
    Please Choose your task:
    1 - calculate factorial
    2 - generate a list of multiples
    3 - find max number in a list
    """)

    while True:
        task = input("Enter task: ")

        try:
            task = int(task)
            
        except ValueError: 
            print("Error: Invalid Input. Please try again.")

        else:
            if task != 1 and task != 2 and task != 3:
                print("Error: Invalid Input")

            else:
                break

    if task == 1:
        

        while True:
            integer = input("Enter a positive integer: ")

            try:
                integer = int(integer)
                
            except ValueError: 
                print("Error: Invalid Input. Please try again.")
            
            else:
                if integer <= 0:
                    print("Error: Invalid Input. Please try again.")
                else:
                    break
        
        print(fun_math.cal_factorial(integer))


    elif task == 2:
        while True:
            number = input("Enter a positive integer number: ")
            length = input("Enter a positive integer length: ")
            try:
                number = int(number)
                length = int(length)
                
            except ValueError: 
                print("Error: Invalid Input. Please try again.")
            
            else:
                if number <= 0 or length <= 0:
                    print("Error: Invalid Input. Please try again.")
                else:
                    break
    
        print(fun_math.list_multiples(number, length))
        

    elif task == 3:
        while True:
            list_length = input("Enter the number of integers in the list: ")

            try:
                list_length = int(list_length)
                
            except ValueError: 
                print("Error: Invalid Input. Please try again.")
            
            else:
                if list_length <= 0:
                    print("Error: Invalid Input. Please try again.")
                else:  
                    break
        while True:
            a_list = [input("Enter integer : ") for x in range(list_length)]

            try:
                j = 0
                while j < list_length:
                    a = int(a_list[j])
                    j += 1

            except ValueError:
                print("Error: Invalid Input. Please try again.")
            else:
                break      
                
        print(fun_math.find_max(a_list))
        
main()
