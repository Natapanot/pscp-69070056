"""[LEARNING LOGS] Bill"""
price = int(input())

service = max(50, min(price * 0.10, 1000)) #max 1000 min 50
total = (price + service) * 1.07 #7%

print(f"{total:.2f}") #.2f ทศนิยม 2 ตำแหน่ง
