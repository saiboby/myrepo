class Employee:
    raise_amt = 1.04
    __sai = 10

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        print('the fullname is {} {}'.format(self.first,self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

############## This is the child class, it inherits from the above parent class #################

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(first,last,pay)
        self.pro_lang = pro_lang

    def display(self):
        print("the names is {}".format(self.first))
        #print("The attribute is {}".format(Employee.__sai))

############## This is the child class, it inherits from the above parent class #################

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super(Manager,self).__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())





dev1 = Developer('sai','t',5000,'python')
#dev2 = Developer('babu','t',6000,'java')
mgr_1 = Manager('sue','smith', 9000,[dev1])

mgr_1.print_emps()

print(Employee.__sai)
mgr_1.remove_emp(dev1)
mgr_1.add_emp(dev2)
mgr_1.print_emps()
mgr_1.fullname()
print(mgr_1.email)
print(dev1.email)
print(dev1.pro_lang)

print(isinstance(mgr_1,Employee)) # it tells whether that instance is belongs to that class or not
print(issubclass(Developer,Employee)) # it tells about the subclasses
