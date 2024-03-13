# Delta-Wye Conversion Script

# Define the conversion functions
def delta_to_wye(Z1, Z2, Z3):
    Za = (Z1 * Z3) / (Z1 + Z2 + Z3)
    Zb = (Z1 * Z2) / (Z1 + Z2 + Z3)
    Zc = (Z2 * Z3) / (Z1 + Z2 + Z3)
    return (Za, Zb, Zc)

def wye_to_delta(Za, Zb, Zc):
    Z1 = ((Za * Zb) + (Zb * Zc) + (Zc * Za)) / Zc
    Z2 = ((Za * Zb) + (Zb * Zc) + (Zc * Za)) / Za
    Z3 = ((Za * Zb) + (Zb * Zc) + (Zc * Za)) / Zb
    return (Z1, Z2, Z3)

# Define the main program
def main():
    while True:
        print("Enter the type of network:")
        print("1. Delta")
        print("2. Wye")
        network_type = int(input())
        if network_type == 1:
            print("Enter the values of Z1, Z2 and Z3:")
            Z1 = float(input())
            Z2 = float(input())
            Z3 = float(input())
            ZA, ZB, ZC = delta_to_wye(Z1, Z2, Z3)
            print(f"The converted Wye values are: ZA={ZA:.2f}, ZB={ZB:.2f}, ZC={ZC:.2f}")
        elif network_type == 2:
            print("Enter the values of ZA, ZB and ZC:")
            ZA = float(input())
            ZB = float(input())
            ZC = float(input())
            Z1, Z2, Z3 = wye_to_delta(ZA, ZB, ZC)
            print(f"The converted Delta values are: Z1={Z1:.2f}, Z2={Z2:.2f}, Z3={Z3:.2f}")
        else:
            print("Invalid input. Try again.")
        print("Do you want to convert another network? (Y/N)")
        repeat = input().lower()
        if repeat != "y":
            break

if __name__ == "__main__":
    main()

