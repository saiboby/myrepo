# we can access the method as an attribute by using property decorator
# in order to pass the value on the demand wish, we can use setter. so that use method as attribute and pass the values
# If we want delete the attribute, we have to use deleter
# class methods are used mainly for class variables alteration and functiong tasks as on of our wish




class Employee:

    count = 0
    __method = 5

    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first+ '.'+ last + '@gmail.com'
        #print(self.email)
    @property
    def fullname(self):
        return "the fullname is {} {}".format(self.first,self.last)
    def meth(self):
        print("The method count is" ,Employee.__method)
    @fullname.setter
    def fullname(self,name):
        first,last =  name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print("Deleting the name")
        self.first = None
        self.last = None
    @classmethod
    def raise_method(cls,mets):
        cls.__method = mets
        print("the new value is",mets)





emp_1 = Employee('john','smith')
emp_1.meth()
emp_1.raise_method(98)
emp_1.meth()

print(Employee.__dict__)
#print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

del emp_1.fullname

emp_1.fullname = 'sai babu'
print(emp_1.fullname)


def funtion1(fun1):
    def function2(a,b):
        print("Going to divide the given numbers")
        if b == 0:
            print("oops!, Can't divide")
            return None

        return fun1(a,b)
    return function2

@funtion1
def function3(c,d):
    #print("please enter the a , b :")
    return int(c/d)

function3(100,0)

def un(*num):
    print("the num is" ,num)
    for n in num:
        print("the given number:", n)

un(1,2,4,6)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

def star(func):
    def inner(*sai):
        print("*" * 30)
        func(*sai)  # this call the main function again i.e,  printer(hello) , when ever the call the function
        print("*" * 30)
    return inner

def percent(func):
    def inner1(*babu):
        print("%"*30)
        func(*babu)
        print("%"*30)
    return inner1
def single(func):
    def inner12(*babu):
        print("1"*30)
        func(*babu)
        print("1"*30)
    return inner12

@single

@star
@percent
def printer(*argss):
    print(*argss)
printer("Hello",1,2,3)
"""

n=0
while n < 5:
    print("less than 5 is count",n)
    n = n+1
else:
    print("not less than 5 are",n)


while True:
    line = input("> ")
    if line == 'done':
        print(line)
        break
	else:
		print('Done!')
		print("something needs to be written")
