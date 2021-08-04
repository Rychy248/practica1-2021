#Using arg arguments

def add(*args):
    """arguments, args is a tuple, in the end"""
    if len(args) > 0:
        sum = 0
        for n in args[:-1]:
            sum += n
            print(n," + ",end="")
        sum += args[-1]
        print(args[-1],end=" = ")
        print(sum)

def calculate(n,**kwargs):
    """Key words arguments, kwargs, it's a dictionary"""
    print(kwargs)
    for key,value in kwargs.items():
        print(key," ",value)
    print("Values = ",kwargs["add"]," ",kwargs["multiply"])
    print()
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print("args","-"*10)
add(2,4,5,7,9,11)
add(1,2,3,4,5)
add(2,4,5,3)
add(1,3,5)
add(2,4)
add(2)
add()

print("\nKwargs","-"*10)
print(calculate(2,add=23,multiply=3))
