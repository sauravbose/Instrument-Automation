import visa
import time

p=visa.instrument("COM3")
p.write("*SYST:REM\r")


def constvolt(p):

    currlimit(p)
    p.write("*CLS")
    p.write("*RST")
    print"Enter the voltage you wish to apply"
    volt=input()
    p.write("*VOLT %f\r"%volt)
    print"The voltage has been set to %f"%volt
    print"\nPress a key to start output voltage"
    raw_input()
    p.write("*OUTP ON\r")

    print"\nPlease wait while output stabilizes..."
    time.sleep(10)
    
    print"\nPress a key to stop output"
    raw_input()
    p.write("*OUTP OFF\r")


def constcurr(p):

    voltlimit(p)
    p.write("*CLS")
    p.write("*RST")
    print"Enter the current you wish to apply"
    curr=input()
    p.write("*CURR %f\r"%curr)
    print"The current has been set to %f"%curr
    print"\nPress a key to start output curent"
    raw_input()
    p.write("*OUTP ON\r")

    print"\nPlease wait while output stabilizes..."
    time.sleep(10)  
        
    print"\nPress a key to stop output"
    raw_input()
    p.write("*OUTP OFF\r")
    

def constpow(p):
    
    p.write("*CLS")
    p.write("*RST")
    print"Enter the power you wish to apply"
    power=input()

    voltlimit(p)
    
    p.write("*CURR 0.5\r")
    p.write("*OUTP ON\r")

    print"\n Please wait. Calculating resistance of load and setting power...\n"
    time.sleep(10)
    
    p.write("*READ?\r")
    a=p.read()

    p.write("*OUTP OFF\r")
    
    a=a.split(' ')   
    v=a[1]
    i=a[3]    
    v=v.split('V')
    i=i.split('A')    
    v=v[0]
    i=i[0]
    v=float(v)
    i=float(i)

    res=v/i
    
    volt=((power*res)**(1.0/2.0))
    
    p.write("*CLS\r")
    p.write("*RST\r")

    currlimit(p)
    
    print"\n Setting voltage...\n"
    
    p.write("*VOLT %f"%volt)
    time.sleep(5)

    print"The power has been set to %f"%power
    print"\nPress a key to start output"
    raw_input()
    p.write("*OUTP ON\r")

    print"\nPlease wait while output stabilizes..."
    time.sleep(10) 

    print"\nPress a key to stop output"
    raw_input()
    p.write("*OUTP OFF\r")


def currlimit(p):
    p.write("*CLS")
    p.write("*RST")
    print"Set the current limit"
    limit1=input()
    p.write("*CURR %f\r"%limit1)
    print"The current limit has been set to %f"%limit1

def voltlimit(p):
    p.write("*CLS")
    p.write("*RST")
    print"Set the volt limit"
    limit2=input()
    p.write("*VOLT %f\r"%limit2)
    print"The voltage limit has been set to %f"%limit2

def menu():
    print"_____________________________MENU_________________________________"
    print"\n1. Constant voltage\n2. Constant Current\n3. Constant Power\n4. Quit"
    print"__________________________________________________________________"
    print"Enter your choice"

choice=0

menu()

while choice!=4:
    choice=input()

    if (choice==1):
        constvolt(p)
        menu()
    elif (choice==2):
        constcurr(p)
        menu()
    elif(choice==3):
        constpow(p)
        menu()
        
p.write("*SYST:LOC\r")
