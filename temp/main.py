x = int(input())
y = int(input())
z = int(input())

if x < y:
    if x < z:
        smallest = x
    else:
        smallest = z
elif y < z:
    smallest = y
else:
    smallest = z

    
print(smallest)

