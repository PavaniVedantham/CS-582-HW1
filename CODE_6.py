def main():

    file_name = input('Enter input filename: ')

    try:
        with open(file_name, "r") as file:
            print('{:<12s} {:>10s} {:>10s}'.format('Name', 'Hours Worked', 'Wages Paid'))
            for line in file: # to calculate the value
                name, hourly_wage, hours_worked = line.strip().split(" ")
                wages_paid = float(hourly_wage) * float(hours_worked)
                print('{:<12s} {:>10d} {:>10.2f}'.format(name, hours_worked, wages_paid))
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: Invalid file format")


        
if __name__ == "__main__":
    main()
