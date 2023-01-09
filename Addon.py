from DataInterfacePython import *

def ModelStart(userData):
    userData["yawFile"] = open("D:/Software/IntelliJ PyCharm Community/Python Projects/Car/yawFile.txt", mode="w+")
    userData["speedFile"] = open("D:/Software/IntelliJ PyCharm Community/Python Projects/Car/speedFile.txt", mode="w+")
    userData["yawFile"].write("exp starts \n")
    userData["speedFile"].write("exp starts \n")
    print("start\n")
    pass

def ModelOutput(userData):
    userData["yawFile"].write('1')
    userData["yawFile"].write('\n')
    userData["speedFile"].write('2')
    userData["speedFile"].write('\n')
    pass

def ModelTerminate(userData):
    userData["yawFile"].close()
    userData["speedFile"].close()
    pass