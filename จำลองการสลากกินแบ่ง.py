import random

def randommize(n):
    RD=random.randrange(0,100) #RD= RanDom
    if RD==n:print("คุณถูกหวย")
    else:print("คุณโดนหวยกินนะ โอ๋ๆ")

    print("เลขที่ออก >> " ,RD)

n=int(input("ท่านซื้อเลข(0-99) >>> ")) 
randommize(n)