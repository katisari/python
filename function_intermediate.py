# Function Intermediate 1
# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().

import random
def randInt(min=0, max=100):
    difference = max-min
    return int(random.random() * difference) + min


# Function Intermediate 2
# Given

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x[1][0] = 15
print(x)


# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students[0]['first_name']='Bryant'
print(students)

# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# For x, how would you change the value 20 to 30?
z[0]['y']=30
print(z)