import math

def main():

    iterations = int(input("Please Enter the number of iterations: "))

    pi = 0
    sign = 1
    i = 0

    while i < iterations:
        pi += sign * (4.0 / (2 * i + 1))
        sign *= -1
        i += 1
    print(f"Approximated value of pi: {pi}")
    
    
if __name__=="__main__":
    main()
