import math

def main():
    int_height = float(input("Enter the initial height of the ball: "))
    no_of_bounces = int(input("Enter the number of times the ball is allowed to bounce: "))
    bounciness = float(input("Enter the bounciness index "))

    distance = int_height

    i=0;
    while i<no_of_bounces:
    
        distance += distance*bounciness
        i += 1
        
    
    print(f"Total distance traveled by the ball: {distance}")
          

if __name__=="__main__":
    main()
