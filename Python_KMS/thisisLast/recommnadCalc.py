from enum import Enum

from naverWeather import *

tempBenchmark = ['14','20','31','41','55']

class ClotheSleevesKinds(Enum):
    Short = 0       #반팔
    Long = 1        #긴팔
    Both = 3        #둘다 가능

class IsNeedOutClothe(Enum):
    IsOutTrue = 0   #외투 있음
    IsOutFalse = 1  #외투 없음

def CalcHtempStandard():
    for i in range(len(tempBenchmark)):
        if temps < tempBenchmark[i]:
            global tempStandard
            tempStandard = tempBenchmark[i]
            #print(tempStandard)
            break
    return tempStandard

def RecommnadUpClothe():
    # 기준치 받아오기
    CalcHtempStandard()

    global upClothe
    if tempStandard <= tempBenchmark[0]:        
        upClothe = ClotheSleevesKinds.Long.value
    elif tempStandard <= tempBenchmark[1]:
        upClothe = ClotheSleevesKinds.Both.value
    elif tempStandard <= tempBenchmark[2]:
        upClothe = ClotheSleevesKinds.Both.value
    elif tempStandard <= tempBenchmark[3]:
        upClothe = ClotheSleevesKinds.Short.value
    elif tempStandard <= tempBenchmark[4]:
        upClothe = ClotheSleevesKinds.Short.value
    else:
        upClothe = ClotheSleevesKinds.Short.value

    #print(upClothe)
    return upClothe

def RecommnadDownClothe():
    # 기준치 받아오기
    CalcHtempStandard()

    global downClothe
    if tempStandard <= tempBenchmark[0]:        
        downClothe = ClotheSleevesKinds.Long.value
    elif tempStandard <= tempBenchmark[1]:
        downClothe = ClotheSleevesKinds.Long.value
    elif tempStandard <= tempBenchmark[2]:
        downClothe = ClotheSleevesKinds.Both.value
    elif tempStandard <= tempBenchmark[3]:
        downClothe = ClotheSleevesKinds.Short.value
    elif tempStandard <= tempBenchmark[4]:
        downClothe = ClotheSleevesKinds.Short.value
    else:
        downClothe = ClotheSleevesKinds.Short.value

    #print(downClothe)
    return downClothe

def RecommnadOutClothe():
    # 기준치 받아오기
    CalcHtempStandard()

    global outClothe
    if tempStandard <= tempBenchmark[0]:        
        outClothe = IsNeedOutClothe.IsOutTrue.value
    else:
        outClothe = IsNeedOutClothe.IsOutFalse.value    

    #print(outClothe)
    return outClothe