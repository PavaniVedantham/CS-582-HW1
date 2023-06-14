import math

def main():
    hourly_wages = float(input("Enter hourly wage: "))
    regular_hours = float(input("Enter total regular hours: "))
    overtime_hours  = float(input("Enter total overtime hours: "))
#to find over time pay
    overtime_pay = overtime_hours * (1.5 * hourly_wages)
#to find over time pay
    total_pay = (regular_hours * hourly_wages) + overtime_pay
    print(f"Hourly Wage: {hourly_wages}")
    print(f"Regular Hours: {regular_hours}")
    print(f"Overtime Hours: {overtime_hours}")
    print(f"Overtime Pay: {overtime_pay}")
    print(f"Total Pay: $ {total_pay}")
   
if __name__ == "__main__":
    main()
