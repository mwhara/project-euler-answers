top_limit = 1000
total = 0
x = 0

while x < top_limit:
    if x % 3 == 0:
        total += x
    elif x % 5 == 0:
        total += x
    x += 1

print total
