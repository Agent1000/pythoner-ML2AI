Km=float(input("เเดินทางไปที่กิโลเมตรที่>>"))
if Km>=0 and Km<50:
    R=Km*2
    print(f"ราคารวม>>>{R:.2f}บาท")
elif Km>=50 and Km<150:
    FB=(49*2)
    W2=(Km-49)*1.5
    Total=W2+FB
    print(f"ราคารวม>>>{Total:.2f}บาท")
elif Km >= 150 and Km < 350:
    FB2 = (49 * 2)+(100*1.5)
    W2 = (Km - 149) * 1
    Total = W2 + FB2
    print(f"ราคารวม>>>{Total:.2f}บาท")
elif Km >=350:
    FB3 = (49 * 2)+(100 * 1.5)+(249*1)
    W2 = (Km - 349) * 0.5
    Total = W2 + FB3
    print(f"ราคารวม>>>{Total:.2f}บาท")

