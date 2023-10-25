n = int(input("Enter: "))
arr = []
while True:
    if n <= 0:
        break
    else:
        pass
    r = n % 16
    if r == 10:
        r = "A"
    if r == 11:
        r = "B"
    if r == 12:
        r = "C"
    if r == 13:
        r = "D"
    if r == 14:
        r = "E"
    if r == 15:
        r = "F" 
    n //= 16
    arr.append(r)
arr.reverse()
print(*arr,sep="")
print(hex(n))