#WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.
from tkinter import TRUE


def check_dist_No(data_list):
    if len(data_list) == len(set(data_list)):
        return True
    else:
        return False
    
print(check_dist_No([1,6,5,8]))     #Prints True
print(check_dist_No([2,2,5,5,7,8])) #Prints False