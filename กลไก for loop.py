# กลไก loop "for"
stop=int(input("กรอกจำนวนครั้งที่ต้องการหยุด >>"))
ANS = 0
for i in range(0,stop,1): #(start,stop,step)
    ANS+=i
    print("รอบที่ ",i,"ผลรวม " ,ANS)
print("ผลรวม = ",ANS)