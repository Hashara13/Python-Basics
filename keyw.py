def prinnt_age(name,age):
    print("name is: ",name)
    print("age is: ",age)
    
prinnt_age("hashara",24)
prinnt_age(name="hashara",age="24")

# Default Arg
def prinnt_age(name,age=29):
    print("name is: ",name)
    print("age is: ",age)
    
prinnt_age("hashara")
prinnt_age(name="hashara",age="24")