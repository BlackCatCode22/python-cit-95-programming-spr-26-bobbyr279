sh = input("Enter Hours:")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40) * (fr * 1.5)
    # print(reg, otp)
    xp = reg + otp
else:
    # print("Regular")
    xp = float(fh) * float(fr)
print("Pay:", xp)

