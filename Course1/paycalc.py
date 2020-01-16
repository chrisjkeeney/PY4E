def computepay():
    h = input("Enter Hours:")
    r = input("Enter Rate:")
    h = float(h)
    r = float(r)
    if h > 40:
        p = (40*r)+(h-40)*r*1.5
    else:
        p = h*r
    return p

print(computepay())
