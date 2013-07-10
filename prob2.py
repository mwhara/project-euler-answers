top_limit = 4000000
term1 = 1
term2 = 2
next_term = 0
even_sum = 0

while next_term <= top_limit:
    if term2 % 2 == 0:
        even_sum += term2

    next_term = term1 + term2
    term1 = term2
    term2 = next_term

print even_sum
