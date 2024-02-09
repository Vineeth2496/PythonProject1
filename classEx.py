'''
class Computer:
    def __init__(self, cpu, ram):
        #print("In INIT")
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(f'Configuration CPU: {self.cpu} RAM: {self.ram}')


com1=Computer('i5',16)
com2=Computer('Ryzen', 8)

#Computer.config(com1)

com1.config()
com2.config()
'''
'''
class computer:
    def __init__(self):
            self.name='Vineeth'
            self.age=26
    #def update(self):
    #    self.age=24
    def compare(self, other):
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c2=computer()
#c1.update()
c1.name='Vikram'
c1.age=27
if c1.compare(c2):
    print('They are same')
else:
    print('They are different')

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)
'''

'''
class Car:
    wheels=4
    def __init__(self):
        self.mileage=10
        self.company='MERC'


c1=Car()
c2=Car()
c1.mileage=8
Car.wheels=6

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)
'''
'''
class Student:
    college='Parul'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    # Accessor Methods & Mutator methods
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value

    @classmethod
    def getCollege(cls):
        return cls.college
    @staticmethod
    def info():
        print("This is student library for PU")

s1=Student(40,50,60)
s2=Student(50,55,65)

print(s1.avg())
print(s2.avg())
#print(s1.m1)       # Used to fetch values
print(Student.getCollege())

Student.info()
'''
# class Student:
#     def __init__(self, name, rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.Laptop()
#
#     def show(self):
#         print(self.name, self.rollno)
#         self.lap.show()
#
#     class Laptop:
#         def __init__(self):
#             self.brand='HP'
#             self.cpu='i5'
#             self.ram=16
#         def show(self):
#             print(self.brand, self.cpu, self.ram)
# s1=Student('Vineeth', 70)
# s2=Student('Katherine', 97)
#
# s1.show()
# s2.show()
#print(s1.lap.brand)
#lap1=s1.lap
#lap2=s2.lap
#print(id(lap1))
#print(id(lap2))

#lap1=Student.Laptop()
#lap1.show()

'''
# Inheritance
class A:
    def feature1(self):
        print('Feature1 is working')
    def feature2(self):
        print('Feature2 is working')
#Single Level Inheritance
#class B(A):
class B:
    def feature3(self):
        print('Feature3 is working')
    def feature4(self):
        print('Feature4 is working')
#Multi Level Inheritance
#class C(B):

#Multiple Inheritance
class C(A,B):
    def feature5(self):
        print('Feature4 is working')

a=A()
#a.feature1()
#a.feature2()

b=B()
#b.feature3()
#b.feature4()
#b.feature2()
#b.feature1()
c=C()
c.feature5()
c.feature4()
c.feature3()
c.feature2()
c.feature1()
'''
'''
#Constructor in Inheritance
#Method Resolution Order (MRO)
class A:
    def __init__(self):
        print('In Class A')
    def feature1(self):
        print('Feature1-A is working')
    def feature2(self):
        print('Feature2 is working')
class B:
    def __init__(self):
        #super().__init__()
        print('In Class B')

    def feature1(self):
        print('Feature1-B is working')
    def feature4(self):
        print('Feature4 is working')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('In Class C')

    def fetu(self):
        super().feature2()
#a1=A()
#b1=B()
c1=C()
c1.feature1()
c1.fetu()
'''

#Ploymorphism
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')
class VSCode:
    def execute(self):
        print('Code Check')
        print('Convention Check')
        print('Compiling')
        print('Running')
class Laptop:
    def code(self, ide):
        ide.execute()

#ide=PyCharm()
ide=VSCode()
lap1=Laptop()
lap1.code(ide)



# class Student:
#     def __init__(self, name, rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.Laptop('Dell', 'i7', '16')
#
#     def show(self):
#         print(self.name, self.rollno)
#         self.lap.show()
#
#     class Laptop:
#         def __init__(self, brand, cpu, ram):
#             self.brand=brand #'HP'
#             self.cpu=cpu   #'i5'
#             self.ram=ram   #16
#         def show(self):
#             print(self.brand, self.cpu, self.ram)
# s1=Student('Vineeth', 70)
# s2=Student('Katherine', 97)
#
# s1.show()
# s2.show()