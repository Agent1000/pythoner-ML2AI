def BMICheck():
    if result < 18:
    	print ("{0:.2f}".format(result)) # เป็นการ format เพื่อทำ ทศนิยม 2 ตำแหน่ง
    	print("Thin")
    elif result >= 18 and result <=22 :
    	print ("{0:.2f}".format(result))  # เป็นการ format เพื่อทำ ทศนิยม 2 ตำแหน่ง
    	print( "Good Health")
    elif result >= 23 and result <=24:
    	print ("{0:.2f}".format(result)) # เป็นการ format เพื่อทำ ทศนิยม 2 ตำแหน่ง
    	print("Fat Level 1")
    elif result >= 25 and result <=29:
    	print ("{0:.2f}".format(result)) # เป็นการ format เพื่อทำ ทศนิยม 2 ตำแหน่ง
    	print("Fat Level 2")
    else : 
    	print ("{0:.2f}".format(result)) # เป็นการ format เพื่อทำ ทศนิยม 2 ตำแหน่ง
    	print("Fat Level 3")

kg = float(input())
cm = float(input())
m2=(cm/100)**2
result=kg/m2
BMICheck()