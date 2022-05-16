def fibonacci(n):
    fibolist = [0, 1]
    index = 1
    f = 0

    while f < n:
        f = fibolist[index-1] + fibolist[index]
        index += 1
        if f < n:
            fibolist.append(f)
    return fibolist

print(fibonacci(21))
print(fibonacci(54))
    
