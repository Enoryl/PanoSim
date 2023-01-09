from DataInterfacePython import *

def ModelStart(userData):
    userData["ego"] = BusAccessor(userData["busId"], "ego", "time@i,x@d,y@d,z@d,yaw@d,pitch@d,roll@d,speed@d")
    userData["yawFile"] = open("D:/Software/IntelliJ PyCharm Community/Python Projects/Car/yawFile.txt", mode="w+")
    userData["speedFile"] = open("D:/Software/IntelliJ PyCharm Community/Python Projects/Car/speedFile.txt", mode="w+")
    userData["yawFile"].write("exp starts \n")
    userData["speedFile"].write("exp starts \n")
    print("start\n")
    pass

def ModelOutput(userData):
    time, x, y, z, yaw, pitch, roll, speed = userData["ego"].readHeader()
    userData["yawFile"].write(str(yaw))
    userData["yawFile"].write('\n')
    userData["speedFile"].write(str(speed))
    userData["speedFile"].write('\n')
    pass

def ModelTerminate(userData):
    userData["yawFile"].close()
    userData["speedFile"].close()
    pass