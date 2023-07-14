import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
symbols = "!@#$%^&*(_)-=+[{]}:'|\/?.>,<"

ans = lower + upper + numbers + symbols

length = 32

password = "".join(random.sample(ans, length))
print("Generated password: ", password)
