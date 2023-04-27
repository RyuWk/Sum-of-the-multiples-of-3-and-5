three = five = fifteen = 0
for n in range(1,1000):
    if n % 3 == 0:
        three += n
    if n % 5 == 0:
        five += n
    if n % 15 == 0:
        fifteen += n
    r = three + five - fifteen
print(f'The sum of all the multiples of 3 and 5 below 1000 is {r}')