cube = lambda x: x ** 3
print(cube(2))

#-----------------------------------------------------------

def multiple_args(*args):
    sum = 0 
    for i in args:
        sum += i
    print(sum)

multiple_args(1,2,3,4)
    

#----------------------------------------------------------

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    

print_kwargs(name="hero", enemy="villan")
print_kwargs(name="hero", enemy="villan",power="nothing")

