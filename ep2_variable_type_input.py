product_name = "กล้อง"
quantity = 18
price = 3.99
is_available = True

print("--- แสดงค่าตัวแปร ---")
print(product_name)
print(quantity)

print("\n--- ตรวจสอบชนิดข้อมูล ---")
print(type(product_name))
print(type(quantity))
print(type(price))
print(type(is_available))

print("\n--- การใช้ input  และการแปลงข้อมูล ---")
user_name = input("กรุณากรอกชื่อของคุณ: ")
birth_year_str = input("กรุณากรอกปีเกิด พ.ศ. : ")
birth_year = int(birth_year_str)

current_year = 2569
age = current_year - birth_year
print(f"สวัสดีคุณ {user_name} ตอนนี้คุณมีอายุ {age}")




