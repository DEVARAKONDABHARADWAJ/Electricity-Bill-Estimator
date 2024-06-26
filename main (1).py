from array import *
def APSPDCL_GROUPA (x):
    if x <= 50:
        price = x * 1.45
        print("The Estimation Price is :" + str(price))
    elif x > 50 and x <= 75:
        price = x * 2.6
        print("The Estimation Price is :" + str(price))

def APSPDCL_GROUPB (y):
    if y <= 100:
        price = y * 2.6
        print("The Estimation Price is :" + str(price))
    elif y > 100 and y <= 200:
        price = y * 3.6
        print("The Estimation Price is :" + str(price))
    elif y > 100 and y <= 300:
        price = y * 6.9
        print("The Estimation Price is :" + str(price))


def APSPDCL_GROUPC (z):
    if z <= 50:
        price = z * 2.65
        print("The Estimation Price is :" + str(price))
    elif z > 50 and z <= 100:
        price = z * 3.35
        print("The Estimation Price is :" + str(price))
    elif z > 100 and z <= 200:
        price = z * 5.4
        print("The Estimation Price is :" + str(price))
    elif z > 200 and z <= 300:
        price = z * 7.1
        print("The Estimation Price is :" + str(price))
    elif z > 300 and z <= 400:
        price = z * 7.95
        print("The Estimation Price is :" + str(price))
    elif z > 400 and z <= 500:
        price = z * 8.5
        print("The Estimation Price is :" + str(price))
    elif z > 500:
        price = z * 9.95
        print("The Estimation Price is :" + str(price))


def enterload():
    entered_load =[]
    load_name = (input("Enter household name :"))
    entered_load.append(load_name)
    load_power = float(input("Enter power rating of load (in Watts) :"))
    entered_load.append(load_power)
    load_time = float(input("Enter duration of usage of the load for a day (24 Hours) :"))
    entered_load.append(load_time)
    load_units=(load_power*load_time)/1000
    entered_load.append(load_units)
    return entered_load


def price_estimaton(units):
    print("Enter Group type :\n1.Group A ST Community people Houses")
    print("\n2.Group B SC Community people Houses")
    m = int(input("\n3.Group C General Houses\n"))
    if m==1 :
        APSPDCL_GROUPA(units)
    elif m==2:
        APSPDCL_GROUPB(units)
    elif m == 3:
        APSPDCL_GROUPC(units)


load = []

total_units=0
i1 = int(input("Welcome to Electricity Bill Estimator\n1.To Calculate New Bill\n2.Exit\n"))
if(i1==1):
    n=int(input("Enter number of Load details you want to enter :"))
    print("Name\tPower\ttime\tunits consumed (1 day)")
    for i in range(n):
        m=i+1
        print("Enter "+ str(m) +"th load details")
        load.append(enterload())
        total_units=total_units+load[i][3]
    print("load Name\t Power Consumed by load  \tPower Consumption Period in a Day\t Units Consumed in One Day" )
    for i in range(n):
        print(load[i][0] + "\t\t\t" + str(load[i][1]) + "\t\t\t" + str(load[i][2]) + "\t\t\t" + str(load[i][3]))
    print("\t\tTotal units consumed in one day  \t\t"+str(total_units))
    total_units_month=total_units * 30
    print("\t\tTotal units consumed in one month\t\t"+str(total_units_month))
    price_estimaton(total_units_month)