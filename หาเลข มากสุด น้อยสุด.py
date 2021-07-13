x=int(input("กรอกเลขครั้งที่ 1  > "))
y=int(input("กรอกเลขครั้งที่ 2  > "))
z=int(input("กรอกเลขครั้งที่ 3  > "))
if z>y and z>x  :print(z,"มากที่สุด")
elif x>y and x>z:print(x,"มากที่สุด")
elif y>x and y>z :print(y,"มากที่สุด")
if z<y and z<x : print(z,"น้อยที่สุด") #if เช็คใหม่ หาเลขน้อยสุด
elif x<y and x<z:print(x,"น้อยที่สุด")
elif y<x and y<z :print(y,"น้อยที่สุด")
# อันนี้ไม่ได้ใช้ loop ช่วย