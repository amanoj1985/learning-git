a = input('enter hours ')
b = input('enter rat')
xx = float(a)
yy = float(b)
if xx > 8:
    print('over time')
    reg = xx * yy
    otp = (xx - xx) * (yy * 0.50)
    print(reg, otp)
    ay = reg + otp
else:
    print('Regular')
    ay = xx * yy
print('Pay', ay)