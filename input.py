username = raw_input("Enter username:") #for python 3 input()
b_year=raw_input("Birth year : ")
weight_p=raw_input("Enter weight : ")
age=2023-int(b_year) #int(b_year) for convert str to int
weight_kg=0.45*float(weight_p)
print("Username is: " + username)
print(age)
print(weight_kg)
print(type(weight_p)) #type of var for input it always string