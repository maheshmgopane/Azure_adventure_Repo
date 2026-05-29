def is_leap(year):
    leap = False
    if (1900 <= year <= 10**5):
        if ((year % 4 ==0)& (year%100 !=0)) |(year % 400==0):
            leap=True
    return leap

year = int(input("Enter a year:",))
a=is_leap(year)
print(a)