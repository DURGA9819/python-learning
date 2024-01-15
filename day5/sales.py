sales = int(input("enter the sales:"))
if sales >= 3000:
    if(sales>= 3000 and sales <= 4000):
        print(" 3% commission")
    elif (sales>=4000 and sales <=5000):
        print("5% comission")
    elif (sales>=5000):
        print("10% comission")
else:
    print("no commision")