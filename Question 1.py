a = input("Put in the input\n")

b = len(a)

print("Length of the string is:\n",b)

c = a[::-1]
print("The reversed string is:\n",c)

d = a[10:26]


a_1 = a.replace("a case sensitive", "object oriented")

print(a_1)


f = a.find("a")
print('Index of "a" substring in input string is:',f)

g = a_1.replace(" ", "")

print(g)
