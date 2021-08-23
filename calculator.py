print("............Welccome to my calculator..............")
for n in range(4):
 calculate=int(input("""
Enter your operation
1. for Add
2. for sub
3. for multi
4. for divide
>>>"""))

 def add(a,b):
    return a+b


 def sub(a,b):
    return a-b

 def multi(a,b):
    return a*b

 def divide(a,b):
    return a/b


x=int(input("Enter any number:"))
y =int(input("Enter any number:"))

if calculate==1:
    adding= add(x,y)
    print(adding)
elif calculate==2:
    subtract=sub(x,y)
    print(subtract)
elif calculate==3:
    multification=multi(x,y)
    print("Total:",multification)

elif calculate==4:
    division=divide(x,y)
    print(division)
else:
    print("Invali operation")            



