# >>>>>>>>>>>>>>>>>>>>>>>>>-1-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def majority_element(nums: list) -> int:
    if not nums:
        return -1
    dct={}
    for x in nums:
        if x not in dct:
            dct[x]=1
        else:
            dct[x]+=1
    return max(dct, key=dct.get)

son=input("Sonlar (masalan: 2,2,1,1,1,2,2) shu tartibda kiritilsin:\n:")

if son.strip() == "":
    nums=[]
else:
    nums=[int(x) for x in son.split(",")]

kop_son=majority_element(nums)
if kop_son != -1:
    print("Eng ko'p takrorlangan son:",kop_son )
else:
    print("bo'sh ro'yxat",kop_son)
