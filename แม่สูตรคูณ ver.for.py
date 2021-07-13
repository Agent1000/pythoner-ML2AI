Msta = int(input("กรอกแม่สูตรคูณเริ่มต้น>>")) # Msta = Mother Start(แม่สูตรคูณเริ่ม)
Msto = int(input("กรอกแม่สูตรคูณสุดท้าย>>")) # Msto = Mother Stop(แม่สูตรคูณที่ให้แสดงเป็นตัวสุดท้าย)
for x in range(Msta,Msto+1):
    print("\nแม่ " , x)
    for y in range(1,13):
        print(x,"x",y,"=" ,x*y)