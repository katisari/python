# 1. Countdown - Create a function that accepts a number as an input.  
# Return a new array that counts down by one, from the number (as arrays 'zero'th element) 
# down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countDown(num):
    array=[]
    for count in range(5,-1,-1):
        array.append(count)
    print(array)

# 2. Print and Return - Your function will receive an array with two numbers. 
# Print the first value, and return the second.
def printreturn(arr):
    print(arr[0])
    return(arr[1])

# 3. First Plus Length - Given an array, return the sum of the first value in the array, 
# plus the array's length.
def sum(arr):
    return arr[0] + len(arr)

# 4. Values Greater than Second - Write a function that accepts any array, 
# and returns a new array with the array values that are greater than its 2nd value.  
# Print how many values this is.  If the array is only element long, have the function return False

def valuegreater(arr):
    if len(arr) == 1:
        return False
    newarr=[]
    counter=0
    for count in range(len(arr)):
        if arr[count] > arr[1]:
            newarr.append(arr[count])
            counter+=1
    print(counter)
    return newarr


# This Length, That Value - Given two numbers, return array of length num1 with each value num2.  
# Print "Jinx!" if they are same.

def thislength(num1, num2):
    newarr=[]
    if num1 == 2:
        print('Jinx!')
    for count in range(num1):
        newarr.append(num2)
    return newarr

# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". 
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def changepositive(arr):
    for count in range(len(arr)):
        if arr[count] > 0:
            arr[count] = 'big'
    return arr
    

# Count Positives - Given an array of numbers, create a function to replace last value with number of 
# positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  
# (Note that zero is not considered to b a positive number).
def countpos(arr):
    counter=0
    for count in range(len(arr)):
        if arr[count] > 0:
            counter+=1
    arr[len(arr)-1] = counter
    return arr


# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values 
# in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(arr):
    sum=0
    for count in range(len(arr)):
        sum+=arr[count]
    return sum

# Average - Create a function that takes an array as an argument and returns the average of all the values
#  in the array.  For example multiples([1,2,3,4]) should return 2.5
def average(arr):
    sum=0
    for count in range(len(arr)):
        sum+=arr[count]
    return sum / len(arr)

# Length - Create a function that takes an array as an argument and returns the length of the array.  
# For example length([1,2,3,4]) should return 4

def length(arr):
    return len(arr)

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.
# If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should 
# return 1; minimum([-1,-2,-3]) should return -3.

def min(arr):
    if(len(arr) == 0):
        return False
    min=arr[0]
    for count in range(1, len(arr)):
        if arr[count] < min:
            min=arr[count]
    return min

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  
# If the passed array is empty, have the function return false.  

def max(arr):
    if(len(arr) == 0):
        return False
    max=arr[0]
    for count in range(1, len(arr)):
        if arr[count] > max:
            max=arr[count]
    return max


# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary 
# that has the sumTotal, average, minimum, maximum and length of the array.

def ultimate(arr):
    max=arr[0]
    min=arr[0]
    sumTotal=0
    average=0
    for count in range(1, len(arr)):
        if arr[count] < min:
            min=arr[count]
        if arr[count] > max:
            max=arr[count]
        sumTotal+=arr[count]
    data={'sumTotal': sumTotal, 'maximum':max, 'minimum': min, 'average': sumTotal/len(arr), 'length': len(arr)}
    return data
    

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed 
# order.  Do this without creating an empty temporary array.  
# For example reverse([1,2,3,4]) should return [4,3,2,1]. 
from math import floor
def reverse(arr):
    for count in range(floor(len(arr)/2)):
        temp=arr[count]
        arr[count]=arr[len(arr)-1-count]
        arr[len(arr)-1-count]=temp
    return arr