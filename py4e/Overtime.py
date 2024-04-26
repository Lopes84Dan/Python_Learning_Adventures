def computepay(hrs, rate):
    if hrs > 40:
        overtime_hours = hrs - 40
        gross_pay = (40 * rate) + (overtime_hours * (1.5 * rate))
    else:
        gross_pay = hrs * rate
    return gross_pay

hrs = int(input("Enter Hours:"))
rate = float(input("Enter Hourly Rate:"))
pay = computepay(hrs, rate)
print("Pay", pay)