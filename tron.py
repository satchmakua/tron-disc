"""This program creates ascii images of "tron-discs" with discrete
user provided input specifiying the number of rings and size of core."""

rings = -1
coreSize = -1

while (rings != 0 or coreSize != 0):

        print("\n")
        rings = abs(int(input("Rings: ")))
        coreSize = abs(int(input("Core Size: ")))
        print("\n")
        ringCount = 1
        coreCount = coreSize
        spaces = rings

        while ringCount != rings+1:
                print((int(spaces-1))*" "+ringCount*"/"+coreSize*"-"+ringCount*"\\")
                spaces -=1
                ringCount +=1      
        ringCount -=1
       
        while coreCount != 0:
                print(rings*'|'+coreSize*' '+rings*'|')
                coreCount -= 1

        while ringCount != 0:
                print((int(spaces))*" "+ringCount*"\\"+coreSize*"-"+ringCount*"/")
                ringCount -=1
                spaces +=1
        continue
    

        
