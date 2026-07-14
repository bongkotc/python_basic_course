print("--- Operators ---")
a = 10
b = 3

print("บวก:", a + b)  # 13
print("ลบ:", a - b)  # 7
print("คูณ:", a * b) #30
print("หาร:", a / b)    #3.333......
print("หารเอาส่วน (ปัดเศษทิ้ง):", a // b)   #3
print("หารเอาเศษ (Modulo):", a % b) #1
print("ยกกำลัง:", a ** b) #1000 <- 10 ยกกำลัง 3

print("\n--- การเปรียบเทียบ (ได้ True/False) ---")
x = 5
y = 8

print("x เท่ากับ y ไหม?:", x == y)    #False
print("x ไม่เท่ากับ y ไหม?:", x != y)  #True
print("x มากกว่า y ไหม?:", x > y)    #False
print("x น้อยกว่า y ไหม?:", x < y)    #True


print("\n--- การใช้ if-elif-else ---")
score = int(input("กรุณากรอกคะแนนของคุณ: "))

if score >= 80:
    print("คุณได้เกรด A")
elif score >= 70:
    print("คุณได้เกรด B")
elif score >= 60:
    print("คุณได้เกรด C")
elif score >= 50:
    print("คุณได้เกรด D")
else:
    print("คุณได้เกรด F")

