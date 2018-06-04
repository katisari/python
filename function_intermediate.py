# Function Intermediate 1
# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().

# import random
# def randInt(min=0, max=100):
#     difference = max-min
#     return int(random.random() * difference) + min


# Function Intermediate 2

# 1. Given

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


# 2. Create a function that given a list of dictionaries, it loops through each dictionary 
# in the list and prints each key and the associated value.  For example, given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# iterateDictionary( students ) should output

# first_name - Michael , last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(arr):
    for count in range(len(arr)):
        result=''
        for keys,values in students[count].items():
            result+= keys + ' - ' + values
            if keys!='last_name':
                result+=' , '
        print(result)

# Create a function that given a list of dictionaries and a key name, it outputs the value stored 
# in that key for each dictionary.  For example, iterateDictionary2('first_name', students)

def iterateDictionary2(key, listdict):
    for count in range(len(listdict)):
        print (listdict[count][key])

iterateDictionary2('first_name', students)



# 4

dojo = {
   'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# Create a function that prints the name of each location and also how many locations the Dojo 
# currently has.  Have the function also print the name of each instructor and how many instructors 
# the Dojo currently has.  For example, printDojoInfo(dojo) should output

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def printDojoInfo(dict):
    print (str(len(dict['location'])) + ' LOCATIONS')
    for count in range(len(dict['location'])):
        print(dict['location'][count])
    print ('\n' + str(len(dict['instructors'])) + ' INSTRUCTORS')
    for count in range(len(dict['instructors'])):
        print(dict['instructors'][count])


printDojoInfo(dojo)