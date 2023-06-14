import statistics as stats
import pandas as pd

def main():
    num = [8,3,4,2,6,7,9]

    
    mean_value = stats.mean(num)
    print("Mean value is:", mean_value)

    
    median_value = stats.median(num)
    print("Median value is:", median_value)

    
    mode_values = stats.mode(num)
    if mode_values is None:
        print("No mode exists.")
    else:
        print(f"Mode value is:{mode_values}")


if __name__ == "__main__":
    main()
