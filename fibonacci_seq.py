def fib_seq():
    a=0
    b=1
    n = int(input("The fibonacci sequence will run this amount of times: "))
    for x in range(n):
        a,b=b,a+b
        yield a
    
if __name__ == '__main__':
	fib_seq()
	for num in fib_seq():
    print(num)