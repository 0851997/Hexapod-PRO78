from time import sleep

def tripodWalking(time):
    #B Vertical Ports=14,1,25  Horizontal Ports=13,0,24  Corresponding legs: Right Front Leg, Right Rear Leg, Left Center Leg
    #A Vertical Ports=30,17,9  Horizontal Ports=29,16,8  Corresponding legs: Left Front Leg, Left Rear Leg, Right Center Leg
    #lynxmotion guide 0 in README
    ser.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    #lynxmotion guide 1 in README
    ser.write("#29P1922#8P1300#16P1478#14P1861#1P1861#25P1139#13P1478#0P1922#24P1300T50\r".encode())
    sleep(0.05)
    #lynxmotion guide 2 in README
    ser.write("#14P1722#1P1722#25P1277T50\r".encode())
    sleep(time)
    #lynxmotion guide 3 in README
    ser.write("#30P1139#9P1861#17P1139T50\r".encode())
    sleep(0.05)
    #lynxmotion guide 4 in README
    ser.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    #lynxmotion guide 5 in README
    ser.write("#30P1139#9P1861#17P1139#29P1522#8P1700#16P1078#13P1078#0P1522#24P1700T50\r".encode())
    sleep(0.05)
    #lynxmotion guide 6 in README
    ser.write("#30P1277#9P1722#17P1277T50\r".encode())
    sleep(time)
    #lynxmotion guide 7 in README
    ser.write("#14P1861#1P1861#25P1139T50\r".encode())
    sleep(0.05)

def reverse(time):
    ser.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    ser.write("#29P1522#8P1700#16P1077#14P1861#1P1861#25P1139#13P1077#0P1522#24P1700T50\r".encode())
    sleep(0.05)
    ser.write("#14P1722#1P1722#25P1277T50\r".encode())
    sleep(time)
    ser.write("#30P1139#9P1861#17P1139T50\r".encode())
    sleep(0.05)
    ser.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    ser.write("#30P1139#9P1861#17P1139#29P1922#8P1300#16P1477#131477#0P1922#24P1300T50\r".encode())
    sleep(0.05)
    ser.write("#30P1277#9P1722#17P1277T50\r".encode())
    sleep(time)
    ser.write("#14P1861#1P1861#25P1139T50\r".encode())
    sleep(0.05)

def turnRight():
    ser.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    ser.write("#29P1922#8P1700#16P1478#14P1861#1P1861#25P1139#13P1078#0P1522#24P1300T50\r".encode())
    sleep(0.05)
    ser.write("#14P1722#1P1722#25P1277T50\r".encode())
    sleep(0.05)
    ser.write("#30P1139#9P1861#17P1139T50\r".encode())
    sleep(0.05)
    ser.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    ser.write("#30P1139#9P1861#17P1139#29P1522#8P1300#16P1078#13P1478#0P1922#24P1700T50\r".encode())
    sleep(0.05)
    ser.write("#30P1277#9P1722#17P1277T50\r".encode())
    sleep(0.05)
    ser.write("#14P1861#1P1861#25P1139T50\r".encode())
    sleep(0.05)

def turnLeft():
    ser.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    ser.write("#29P1522#8P1300#16P1078#14P1861#1P1861#25P1139#13P1478#0P1922#24P1700T50\r".encode())
    sleep(0.05)
    ser.write("#14P1722#1P1722#25P1277T50\r".encode())
    sleep(0.05)
    ser.write("#30P1139#9P1861#17P1139T50\r".encode())
    sleep(0.05)
    ser.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500T50\r".encode())
    sleep(0.05)
    ser.write("#30P1139#9P1861#17P1139#29P1922#8P1700#16P1478#13P1078#0P1522#24P1300T50\r".encode())
    sleep(0.05)
    ser.write("#30P1277#9P1722#17P1277T50\r".encode())
    sleep(0.05)
    ser.write("#14P1861#1P1861#25P1139T50\r".encode())
    sleep(0.05)

def strafeRight():
    print("s")

def strafeLeft(time):
    ser.write("#30P1477#25P1477#17P1477 #14P1522#9P1522#1P1522 T50\r".encode())             #Higher standing stance
    sleep(time)
    ser.write("#25P1177 #9P1822 T50\r".encode())                                            #Center legs position high
    sleep(time)
    ser.write("#26P1255 #10P2144 T50\r".encode())                                           #Center legs position high leftside
    sleep(time)
    ser.write("#25P1477 #9P1522 T50\r".encode())                                            #Center legs position low leftside
    sleep(time)
    ser.write("#14P1822 #1P1822 T50\r".encode())                                            #Rightfront and rightrear legs position high (left side is pulling)
    sleep(time)
    ser.write("#29P1522 #26P1055 #16P1478 #13P1478 #10P1944 #0P1522 T50\r".encode())        #Movement state left to right
    sleep(time)
    ser.write("#14P1522 #1P1522 T50\r".encode())                                            #Rightfront and rightrear legs position low
    sleep(time)
    ser.write("#25P1177 #9P1822 T50\r".encode())                                            #Center legs high possition
    sleep(time)
    ser.write("#26P1255 #10P2144 T50\r".encode())                                           #Center legs position high leftside 
    sleep(time)
    ser.write("#25P1477 #9P1522 T50\r".encode())                                            #Center legs position low leftside
    sleep(time)
    ser.write("#30P1177 #17P1177 T50\r".encode())                                           #Leftfront and leftrear legs position high
    sleep(time)
    ser.write("#29P1722 #26P1055 #16P1278 #13P1278 #10P1944 #0P1722 T50\r".encode())        #Movement state2 left to right (right side is pushing)
    sleep(time)