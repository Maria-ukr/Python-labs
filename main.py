# First program
a_input = input("Enter first number: ")

while not (a_input.isdigit() and int(a_input) > 0):
  a_input = input("Please enter a non-negative first number: ")
a = int(a_input)

b_input = input("Enter second number: ")

while not (b_input.isdigit() and int(b_input) > 0):
  b_input = input("Please enter a non-negatlive second number: ")
b = int(b_input)

if a == b:
  result = -1

elif a < b:
  result = a/b + 1

else:
  result = (a * b - 5) / a

print("The result is:", result)






# Second program
n_input = input("Enter a number from 1 to 10: ")

while not (n_input.isdigit() and int(n_input) > 0 and int(n_input) < 10):
  n_input = input("Please enter a number from 1 to 10: ")

N = int(n_input)

for i in range(N, 0, -1):
  for j in range(0, N, 1):
    if j > i - 1:
      print(" ", end=" ")
    else:
      print(N, end = " ")
  print("")

for i in range(1, N + 1, 1):
  for j in range(0, N, 1):
    if j > i - 1:
      print(" ", end=" ")
    else:
      print(N, end = " ")
  print("")






# Third program
from mod import countingNumbers

x_input = input("Enter a positive number: ")

while not (x_input.isdigit() and int(x_input) > 0):
  x_input = input("Please enter a positive number: ")

countingNumbers(int(x_input))

n = 0
while n <= 20:
  if n % 2 == 0 and not n == 0:
    print(n)
  n += 1