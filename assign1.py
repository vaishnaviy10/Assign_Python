#adding prime numbers to list

def isprimeNo(n):
    if (n < 2):
        return False
    else:
        for i in range(2, int(n ** 0.5) +1):
            if (n%2) == 0:
                return False
        return True

def findprime(lim):
    prime = []
    for n in range(2,lim + 1):
        if isprimeNo(n):
            prime.append(n)
    return prime

lim = 50
result = findprime(lim)
print(result)

#user input table

def print_table(n):
    for i in range(1, 11):
        result = n*i
        print(n," * ", i ," = ", result)

n = int(input("enter number : "))
print_table(n)

#Palindrome String
 
str = input("enter word : ")
if (str == str[::-1]):
    print("word ",str," is palindrome")
else:
        print("word ",str," is not palindrome")

#reverse string

s = input("enter string : ")
print("reverse string is : ", s[::-1])
