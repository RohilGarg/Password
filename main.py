import math

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = input("Enter a password: ")
length = len(password)
low = 0
up = 0
num = 0
spec = 0
for i in password:
  if i in lower:
    low = 26
  elif i in upper:
    up = 26
  elif i in numbers:
    num = 10
  else:
    spec = 32
entropy = length * math.log2(low+up+num+spec)
entropy = round(entropy, 0)
for i in range(len(password)-1):
  print(entropy)
  if password[i] in lower:
    if password[i+1] in lower:
      entropy -= 2
  elif password[i] in upper:
    if password[i+1] in upper:
      entropy -= 2
  elif password[i] in numbers:
    if password[i+1] in numbers:
      entropy -= 2
  else:
    if ~(password[i+1] in [lower, upper, numbers]):
      entropy -= 2
print(entropy)

if entropy < 20:
  print("Very low")
elif entropy < 40:
  print("Low")
elif entropy < 60:
  print("Medium")
elif entropy < 80:
  print("High")
else:
  print("Very high")