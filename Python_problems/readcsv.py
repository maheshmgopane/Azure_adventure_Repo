n=int(input("Enter a number:"))
print(n)
if (n%2 ==0) & ((n in range(2,6))|(n > 20)):
    print("Not Weird")
else:
    print("Weird") 