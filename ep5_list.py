print("ส่วนที่ 1 การสร้าง List และการเข้าถึงข้อมูล (index & slice)")
fruits = ["apple", "banana", "cherry", "orange"]
#           0          1        2           3
#การเข้าถึงข้อมูล index
print(fruits)
print(fruits[0])
print(fruits[-1])
#การตัดช่วงข้อมูล slice [เริ่มต้น:ก่อนถึงตัวจบ]
print(fruits[1:3])

print("ส่วนที่ 2 ฟังก์ชันการจัดการ List (.append, .remove, .sort)")
number = [5,2,9,1]
print(number)
#เพิ่มข้อมูลต่อท้าย .append
number.append(7)
print(number)
#ลบข้อมูล .remove
number.remove(2)
print(number)
#เรียงลำดับข้อมูล .sort
number.sort()
print(number)

print("ตัวอย่าง")
students = []
students.append("Somchai")
students.append("Somsri")
students.append("Somsak")
print("รายชื่อนักเรียนทั้งหมด: ",students)
#มีนักเรียนลาออก 1 คน
students.remove("Somsri")
print("อัปเดตรายชื่อหลังมีคนลาออก: ", students)

