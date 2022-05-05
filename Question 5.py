side1 = float(input("Enter length 1\n"))
side2 = float(input("Enter length 2\n"))
side3 = float(input("Enter length 3\n"))

side_1 = int(round(side1))
side_2 = int(round(side2))
side_3 = int(round(side3))

a = side_1 + side_2
b = side_2 + side_3
c = side_1 + side_3

check_1 = a > side_3
check_2 = b > side_1
check_3 = c > side_2

answer = str(check_1 & check_2 & check_3)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")

print(answer)
