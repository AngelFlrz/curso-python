import random

# for
print("for")

x = 0

for i in range(10):
    print(i)
    x += random.randint(1, 5)

print(x)

# while
print("while")
y = 0
while y != 5:
    y = random.randint(1, 100)
    print(y)
