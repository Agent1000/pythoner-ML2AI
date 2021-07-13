m=0
while m!=4:
    print("menu")
    print("1. input data")
    print("2. output data")
    print("3. exit program")
    Ch= int(input("เลือกตัวเลือกที่ท่านต้องการ>>>"))
    if Ch==1:
        x=int(input("Menu 1 input data \nกรอกเลขสูตรคูณ>>>"))
    elif x==0:
        print("ท่ายยังไม่กรอกเมนู 1")
    elif Ch==2:
        print("Menu 2 output data")
        for n in range(1,13):
            Total=x*n
            print(f"{x}*{n}={Total}")
    elif Ch==3:
        print("Menu 3 Exit program")
        break
print("good bye")


