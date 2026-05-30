# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
m = int(input())

if b < 0:
    print("Error: b cannot be negative when m is provided.")
else:
    if 1 <= a <= 10 and 1 <= b <= 10 and 2 <= m <= 1000:
        print(pow(a, b))        
        print(pow(a, b, m))
        if (a // b)>1:
            print(a // b)
