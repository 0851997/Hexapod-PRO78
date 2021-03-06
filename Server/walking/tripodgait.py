from time import sleep
import standing.stableStance as standing

#B Vertical Ports=14,1,25  Horizontal Ports=13,0,24  Corresponding legs: Right Front Leg, Right Rear Leg, Left Center Leg
#A Vertical Ports=30,17,9  Horizontal Ports=29,16,8  Corresponding legs: Left Front Leg, Left Rear Leg, Right Center Leg


def tripodWalking(config):
    #lynxmotion guide 0 in README
    config.serialConn.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500\r".encode())
    #lynxmotion guide 1 in README
    config.serialConn.write("#29P1922#8P1300#16P1478#14P1861#1P1861#25P1139#13P1478#0P1922#24P1300\r".encode())
    #lynxmotion guide 2 in README
    config.serialConn.write("#14P1722#1P1722#25P1277\r".encode())
    #lynxmotion guide 3 in README
    config.serialConn.write("#30P1139#9P1861#17P1139\r".encode())
    #lynxmotion guide 4 in README
    config.serialConn.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500\r".encode())
    #lynxmotion guide 5 in README
    config.serialConn.write("#30P1139#9P1861#17P1139#29P1522#8P1700#16P1078#13P1078#0P1522#24P1700\r".encode())
    #lynxmotion guide 6 in README
    config.serialConn.write("#30P1277#9P1722#17P1277\r".encode())
    #lynxmotion guide 7 in README
    config.serialConn.write("#14P1861#1P1861#25P1139\r".encode())

def reverse(config):
    config.serialConn.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500\r".encode())
    config.serialConn.write("#29P1522#8P1700#16P1077#14P1861#1P1861#25P1139#13P1077#0P1522#24P1700\r".encode())
    config.serialConn.write("#14P1722#1P1722#25P1277\r".encode())
    config.serialConn.write("#30P1139#9P1861#17P1139\r".encode())
    config.serialConn.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500\r".encode())
    config.serialConn.write("#30P1139#9P1861#17P1139#29P1922#8P1300#16P1477#131477#0P1922#24P1300\r".encode())
    config.serialConn.write("#30P1277#9P1722#17P1277\r".encode())
    config.serialConn.write("#14P1861#1P1861#25P1139\r".encode())

def turnRight(config):
    config.serialConn.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500\r".encode())
    config.serialConn.write("#29P1822#8P1600#16P1378#14P1861#1P1861#25P1139#13P1178#0P1622#24P1400\r".encode())
    config.serialConn.write("#14P1722#1P1722#25P1277\r".encode())
    config.serialConn.write("#30P1139#9P1861#17P1139\r".encode())
    config.serialConn.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500\r".encode())
    config.serialConn.write("#30P1139#9P1861#17P1139#29P1622#8P1400#16P1178#13P1378#0P1822#24P1600\r".encode())
    config.serialConn.write("#30P1277#9P1722#17P1277\r".encode())
    config.serialConn.write("#14P1861#1P1861#25P1139\r".encode())

def turnLeft(config):
    config.serialConn.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500\r".encode())
    config.serialConn.write("#29P1622#8P1400#16P1178#14P1861#1P1861#25P1139#13P1378#0P1822#24P1600\r".encode())
    config.serialConn.write("#14P1722#1P1722#25P1277\r".encode())
    config.serialConn.write("#30P1139#9P1861#17P1139\r".encode())
    config.serialConn.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500\r".encode())
    config.serialConn.write("#30P1139#9P1861#17P1139#29P1822#8P1600#16P1378#13P1178#0P1622#24P1400\r".encode())
    config.serialConn.write("#30P1277#9P1722#17P1277\r".encode())
    config.serialConn.write("#14P1861#1P1861#25P1139\r".encode())

def strafeLeft(config):
    standing.stableStance(config)
    config.serialConn.write("#30P1477#25P1477#17P1477 #14P1522#9P1522#1P1522 \r".encode())             #Higher standing stance
    config.serialConn.write("#25P1177 #9P1822 \r".encode())                                            #Center legs position high
    config.serialConn.write("#26P1255 #10P2144 \r".encode())                                           #Center legs position high leftside
    config.serialConn.write("#25P1477 #9P1522 \r".encode())                                            #Center legs position low leftside 
    config.serialConn.write("#14P1822 #1P1822 \r".encode())                                            #Rightfront and rightrear legs position high (left side is pulling)
    config.serialConn.write("#29P1522 #26P1055 #16P1478 #13P1478 #10P1944 #0P1522 \r".encode())        #Movement state left to right
    config.serialConn.write("#14P1522 #1P1522 \r".encode())                                            #Rightfront and rightrear legs position low
    config.serialConn.write("#25P1177 #9P1822 \r".encode())                                            #Center legs high possition
    config.serialConn.write("#26P1255 #10P2144 \r".encode())                                           #Center legs position high leftside 
    config.serialConn.write("#25P1477 #9P1522 \r".encode())                                            #Center legs position low leftside
    config.serialConn.write("#30P1177 #17P1177 \r".encode())                                           #Leftfront and leftrear legs position high
    config.serialConn.write("#29P1722 #26P1055 #16P1278 #13P1278 #10P1944 #0P1722 \r".encode())        #Movement state2 left to right (right side is pushing)

def strafeRight(config):
    standing.stableStance(config)
    config.serialConn.write("#30P1477#25P1477#17P1477 #14P1522#9P1522#1P1522 #26P1255 #8P1600 \r".encode())             #Higher standing stance
    config.serialConn.write("#25P1177 #9P1822 \r".encode())                                            #Center legs position high
    config.serialConn.write("#26P1055 #10P1744 \r".encode())                                           #Center legs position high rightside "left center leg might not be right"
    config.serialConn.write("#25P1477 #9P1422 \r".encode())                                            #Center legs position low rightside
    config.serialConn.write("#30P1177 #17P1177 \r".encode())                                           #leftfront and leftrear legs position high (right side is pulling)
    config.serialConn.write("#29P1522 #26P1255 #16P1478 #13P1478 #10P1944 #0P1522 \r".encode())        #Movement state right to left
    config.serialConn.write("#30P1477 #17P1477 \r".encode())                                           #Leftfront and leftrear legs position low
    config.serialConn.write("#25P1177 #9P1822 \r".encode())                                            #Center legs high possition
    config.serialConn.write("#26P1055 #10P1744 \r".encode())                                           #Center legs position high rightside 
    config.serialConn.write("#25P1477 #9P1522 \r".encode())                                            #Center legs position low rightside
    config.serialConn.write("#14P1822 #1P1822 \r".encode())                                            #Rightfront and rightrear legs position high
    config.serialConn.write("#29P1722 #26P1255 #16P1278 #13P1278 #10P1944 #0P1722 \r".encode())        #Movement state2 right to left (left side is pushing)
