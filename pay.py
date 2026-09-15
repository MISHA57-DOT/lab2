hours=int(input("Enter hours:"))
rate=int(input("Enter rate:"))
if hours<=40:
    gross_pay=hours*rate
    print("gross pay is",gross_pay)
else:
    gross_pay=40*rate
    over_time=hours-40
    over_time_rate=over_time*rate*1.5
    gross_pay=gross_pay+over_time_rate
    print("gross pay is:",gross_pay)