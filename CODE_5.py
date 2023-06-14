def main():
    purchase_price = float(input(" Please enter the purchase price: "))
    down_payment = purchase_price * 0.1
    interest_rate = 0.12
    monthly_rate = interest_rate / 12
    monthly_payment = purchase_price * 0.05 - down_payment

    balance = purchase_price - down_payment
    print("The payment schedule is:")

    print("Month\t Balance\t Interest\t Principal\t Payment\t Remaining")
    
    month=0
    while True:
        interest = balance * interest_rate / 12
        principal = monthly_payment - interest
        remaining_balance = balance - principal
        if remaining_balance <= 0:
            break
        month += 1
        

        print(month, "\t$" + format(balance, ".2f"), "\t$" + format(interest, ".2f"), "\t$" + format(principal, ".2f"), "\t$" + format(monthly_payment, ".2f"), "\t$" + format(balance, ".2f"))
       

    if __name__=="__main__":
        main()
