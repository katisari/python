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