print("ตัวอย่าง while loop")

countdown = 5
print("เริ่มนับถอยหลัง")
while countdown > 0:
    print(f"เหลือเวลาอีก {countdown} วินาที!")
    countdown = countdown - 1

print("นับเสร็จแล้ว")

print("ตัวอย่างของ for loop")
items = ["แอปเปิ้ล", "กล้วย", "สินค้าชำรุด", "ส้ม", "มะพร้าว"]
print("เริ่มตรวจเช็คสินค้า")

for item in items:
    if item == "สินค้าชำรุด":
        print("เจอสินค้าชำรุด! ข้ามชิ้นนี้ไปก่อน")
        continue

    if item == "ส้ม":
        print(f" เจอ {item} แล้ว! (หยุดการค้นหาตามที่ตั้งเป้าไว้)")
        break
    
    print(f"ตรวจเช็คผ่าน: {item}")

print("จบการทำงาน")