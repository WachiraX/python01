fruitsTuple = ("apple","banana","cherry","kiwi")
fruitsList =["apple","banana","cherry","kiwi"]
print(fruitsTuple[1:2])
print(fruitsList[0])
#เปลี่ยนค่าในtuple
fruitsList[1]="mango"#เปลี่ยนในList
print(fruitsList)
#tupleไม่สามารถเปลี่ยนค่าโดยตรงได้ต้องเปลี่ยนเป็นListก่อน
x = list(fruitsTuple)
x[1]="mango"
fruitsTuple = tuple(x)
print(fruitsTuple)
#เพิ่มค่าในtuple
x = list(fruitsTuple)
x.append("orange")
fruitsTuple =tuple(x)
print(fruitsTuple)
#ลบค่าในtuple
x = list(fruitsTuple)
x.remove("kiwi")
fruitsTuple =tuple(x)
print(fruitsTuple)
x= range(3,20)
for n in x:
    print(n)
x= range(3,20,3)
for n in x:
    print("step3:",n)
#นัชธ์ชาญยุทธ พัชรทับอุไร 14