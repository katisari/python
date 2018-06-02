# 1 Basic - Print all the numbers/integers from 0 to 150.
for count in range(0,151):
    print(count)

# 2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for count in range(5, 1000001, 5):
    print(count)

# 3 Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. 
# If by 10, also print " Dojo".

for count in range(1, 101):
    if count % 5 == 0:
        print('Coding')
    if count % 10 == 0:
        print('Dojo')
    else:
        print(count)

#  4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for count in range(1,500000,2):
    sum+= count
print(sum)

# 5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

for count in range(2018,0,-4):
    print (count)

# 6 Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, 
# print multiples of mult from lowNum to highNum, using a FOR loop.  
# For (2,9,3), print 3 6 9 (on successive lines)

def flexcount(lowNum, highNum, mult):
    for count in range(lowNum, highNum + 1):
        if count % mult == 0:
            print(count)



# Predicting Output!
list = [3,5,1,2]
for i in list:
    print(i)
# OUTPUT: 3,5,1,2

list = [3,5,1,2]
for i in range(list):
    print(i)
# OUTPUT: ERROR

list = [3,5,1,2]
for i in range(len(list)):
    print(i)
# OUTPUT: 0,1,2,3
