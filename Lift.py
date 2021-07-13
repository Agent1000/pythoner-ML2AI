s=0
while s==0:
    print("ระบบคำนวณน้ำหนักในลิฟต์")
    print("ถ้าไม่มีใครเข้าลิฟต์ ให้ใส่น้ำหนักเป็น 0")
    H=int(input(f"**เข้าไปทั้งหมด"))
    if H>6:
        print("คนเกิน")
    else:break
#รับได้ 449 kg ไม่เกิน 6 คน (H<=6)
a=1
while a==1:
    H1 = float(input(f"1 หนัก "))
    if H1>449:
        H1=0
        print(H1)
    H2 = float(input(f"2 หนัก "))
    if H1+H2>449:
        H2 = 0
        print(H2)
    H3 = float(input(f"3 หนัก "))
    if H1 + H2 + H3 > 449:
        H3 = 0
        print(H3)
    H4= float(input(f"4 หนัก "))
    if H1 + H2 +H3 +H4 > 449:
        H4 = 0
        print(H4)
    H5 = float(input(f"5 หนัก "))
    if H1 + H2 + H3 + H4 + H5 > 449:
        H5 = 0
        print(H5)
    H6 = float(input(f"6 หนัก "))
    if H1 + H2 + H3 + H4 + H5 + H6 > 449:
        H6 = 0
        print(H6)
    break
if H1 + H2 + H3 + H4 + H5 + H6 <=449:
    total=H1 + H2 + H3 + H4 + H5 + H6
    print(f"รวม {total:.2f}Kg")
    print("have a nice day")
