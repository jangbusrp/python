# class intro():
#     def __init__(self, name, age, hobby):
#         self.name=name
#         self.age= age 
#         self.hobby = hobby

#     def hobbies(self):
#         print(f"My hobby are plaing {self.hobby}")
#         print(f"My name is {self.name}")
#         print(f"My age is {self.age}")
      

# myhobby = intro("jangbu", 20, "football")
# print(myhobby.hobbies())

# f = open("text.txt", "r")
# print(f.read())

#f.close()

# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

# OOP Exercise 2: Create a Vehicle class without any variables and methods
 
# class vehicle:

#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
       

#     def TATA(self):
#         return(f" TATA max spped is {self.max_speed} km per hour and {self.mileage} mileage per hr")

#     def Tesla(self):
#         return (f" Tesla max spped is {self.max_speed} km and {self.mileage} mileage per hr")

# v1 = vehicle(50, "30 km")
# v2 = vehicle( 80, "80 km")
# print(v2.Tesla()) 
# print(v1.TATA())



#property decorators

# class student:
#     def __init__(self, name):
#         self._name = name 

#     @property
#     def name(self):
#         print("*****this is getter name:")
#         return self._name

#     @name.setter
#     def name(self, name):
#         print("thei is setter mew name:")
#         if len(name)>5:
#             self._name =  name 
#         else:
#             print("Name should be grater then 5")
#     @name.deleter
#     def name(self):
#         print("name has been deleted successfylly")
#         self._name = None

# # s1 = student("jangbu")
# # s2 = student("hari")
# # print(s1.name)
# # s2.name ="jang"
# # print("set", s2._name)
# # #del s1.name
# # print(s1.__dict__)

# # student.mro()
# # a = [(1,2),(3,10),(5,-1)]
# # a.sort(key=lambda x: x[1])
# # print(a)


# class main:
#     def __init__(self, name):
#         self.name = name

#     def walk(self, name):
#         return f" this is main class name {name}"

# class animal:        
#     def dog(self, name):
#         return f" animal class name {name}"

#     def walk(sefl):
#         return ("dog can walk") 


# pol = main("hello") 
# l = animal()

# print(pol.walk("hellll"))
# print(l.walk())
# print(l.dog("bangle"))




   
# from abc import ABC, abstractmethod

# class person(ABC):
#     @abstractmethod
#     def name(self,address):
#         pass

# class ram(person):
#     def name(self):
#         return "my name is ram" 

# class shym(person):
#     def name(self):
#         return "my name is shyam"



# r= ram()
# s = shym()
# print(r.name())
# print(s.name())



from abc import ABC, abstractmethod
class operation(ABC):
    
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def add(self):
        pass
      
    @abstractmethod
    def subs(self):
        pass


class addsum(operation):
    def add(self):
        return (self.value+ 10)

    def subs(self):
        return ( self.value - 10  )

s = addsum(100)
print(s.add())
print(s.subs())   