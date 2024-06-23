sum1=0
def sum_num(num1,num2):
    num1=5
    num2=4
    sum1=num1+num2
    return sum1


result=sum1  
print(sum1)

# use global var
sum1=0
def sum_num(num1,num2):
    num1=5
    num2=4
    global sum1
    return sum1
result=sum1  
print(sum1)