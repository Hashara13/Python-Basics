num=[4,5,74,3,1]    # we can replace [] ny () for **tupples
num2=num.copy()     # make a copy not changing according to first one

num.append(2)       # add new element
num.sort()          # sort ascending
num.reverse()       # sort descending
num.insert(0,9)     # insert new value in 0 place
num.remove(4)       # remone one element
num.pop()           # remove last element
num.clear()         # clear all
print(num.index(5)) # check given number is available 
print(5 in num)     # check given number is available 
print(num.count(5)) # check how many count in given number is available

a,b,c=num      # unpacking listed elements to variables respectively
print(a*b*c)