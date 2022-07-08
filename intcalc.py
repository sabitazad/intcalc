import os
is_pv = "pv"
is_fv = "fv"

os.system('color F')
mode = input("Select calculator (PV or FV): ")
print()
def pv(fv, r, n):
    return fv / (1 + r) ** n
if mode == is_pv:
    while True:
        try:
            fv = int(input("Future value (FV): "))         
            r = float(input("Interest rate: "))
            n = int(input("Number of years: "))
            break
        except ValueError:
            print()
            print("Please input a valid number")
            print()
            continue
    result = pv(fv, r, n)
    print()
    os.system('color B'), print("Answer, Present value (PV) =",result,"TAKA")

elif mode == is_fv:
    def fv(pv, r, n):
        return pv * (1 + r) ** n
    while True:
        try:
            pv = int(input("Present value (PV): "))         
            r = float(input("Interest rate: "))
            n = int(input("Number of years: "))
            break
        except ValueError:
            print()
            print("Please input a valid number!")
            print()
            continue
    result = fv(pv, r, n)
    print()
    os.system('color B'), print("Answer, Future Value (FV) =",result,"TAKA")
else: print("Invalid calculator type")

print()
input('Press ENTER to exit')





