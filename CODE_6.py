def main():

    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as file:
            print("Name\t\tHours Worked\t\tWages Paid")
            for line in file:
                name, hourly_wage, hours_worked = line.strip().split(" ")
                wages_paid = float(hourly_wage) * float(hours_worked)
                print(f"{name}\t\t{hours_worked}\t\t${wages_paid:.2f}")
    except FileNotFoundError:
        print("Error: Could not read file")

        
if __name__ == "__main__":
    main()
