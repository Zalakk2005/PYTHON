print("LETS CALCULATE\n")
print("Operations to perform")

A=print("A.ADD")
B=print("B.SUB")
C=print("C.MULT")
D=print("D.DIV")

print()
chose = input("Select the operator to perform:")
print()


num1 = int(input("Enter first digit:"))
num2 = int(input("Enter second digit:"))

if chose == 'A' :
  print(num1+num2)
elif chose == 'B' :
  print(num1-num2)
elif chose == 'C' :
   print(num1*num2)
elif chose == 'D' :
   print(num1/num2)
else :
  print("Invalid entery")

         
