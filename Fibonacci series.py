def fibonacci(n):
    first =0
    second = 1
    if n == 0:
        print("the reqeisted series is ",f)
    else:
        print(first)
        print(second)
        for i in range(2,n):
            c = first + second
            first = second
            second = c
            print(c)
        

print(fibonacci(5))