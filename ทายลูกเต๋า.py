import random

AnsRandom=random.randrange(1,7)
R= 1 # R แทนรอบในการตอบ
while True : 
    NO=int(input("ช่องตอบเลข >>> "))
    if NO<=0 or R==3:
        break
    right = (NO==AnsRandom)

    if right: 
        print("ถูกต้องแล้วคร้าบบบบบ")
        break
    if not right:
        if(NO>AnsRandom):
            print("น้อยลง")
        if(NO<AnsRandom):
            print("มากขึ้น")
    R+=1

print(" จบบบโปรแกรม")
print("เฉลย" , AnsRandom)