counter = 0

for i in range(201):
    if i % 6:
        contador += 1
        if 1 <= i <= 10:
            i += i

print(counter, i)
