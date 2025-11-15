# x = 4
# print(x)


# def hello():
#     x = 5
#     print(f"The local x is {x}")
#     print("Hello harry")

# print(f"The global x is {x}")
# hello()
# x = 5
# print(f"The local x is {x}")



# another one


x = 10 #global variable

def my_function():
    global x
    x = 5 #this will change the value of the global variable x
    y = 5 #local variable

my_function()    
print(x) # prints 5
# print(y) # this will cause an error because y is a local variables and is not accesible outside of the function

    