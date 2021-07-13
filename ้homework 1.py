student=[]
while True:
    name=str(input("ป้อนชื่อของคุณ :"))
    if name == "จบ":
        break
    student.append(name)

print(student)
student.sort()
print(student)
student.reverse()
print(student)