fruit=["มะม่วงดอง","แตงโมปั่น","ฝรั่งแซ่บ๊วย"]
price=[50,30,15]
fruitShop = {"มะม่วงดอง":{
            "name":"มะม่วงดอง",
            "price":50
},
            "แตงโมปั่น":{
            "name" :"แตงโมปั่น",
            "price" : 30
},
            "ฝรั่งแซ่บ๊วย":{
            "name" :"ฝรั่งแซ่บ๊วย",
            "price": 15 
}}

if "ฝรั่งแซ่บ๊วย" in fruitShop["ฝรั่งแซ่บ๊วย"]["name"]:
    print("เป็น")
else :
    print("ไม่เป็น")