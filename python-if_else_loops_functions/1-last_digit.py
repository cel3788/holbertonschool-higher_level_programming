#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit *= -1

str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"

if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} {str1}")
elif lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} {str2}")
else:
    print(f"Last digit of {number} is {lastdigit} {str3}")

File 2-print_alphabet
#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(i)), end="")
