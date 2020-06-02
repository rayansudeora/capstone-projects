def fib_seq():
    a=0
    b=1
    n = int(input("The fibonacci sequence will run this amount of times: ")) 
    for x in range(n): #user gives the value which dictates how many times the program will run
        a,b=b,a+b #fibonacci sequence (the next number is the sum of the previous two.)
        yield a
    

for num in fib_seq():
    print(num)