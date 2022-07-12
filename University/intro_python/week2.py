time = float(input("Enter a time: "))
t, g = 0, 9.8
while t <= time:
    d = 0.5*g*t**2
    print(f"{str(d)}is the height of the {t}th second")
    t += 1
