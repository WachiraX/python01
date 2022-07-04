#for จะเป็น definite loop หรือ loopที่มีการทำงานที่ชัดเจน
#forกับ
for i in range(1,11,1):
    print(i)
print("finish")
#for กับ list
list1 = ["apple","blueberry","kiwi","papaya"]
for element in list1:
    print(element)
#for กับ dic
dic1 = {"name":"nutchanyut","age":17,"hobbies":"play badmintion"}
for key,value in dic1.items():
    print(key,value)
#while indefinite loop หรือ loopที่ทำงานไม่ชัดเจน
i =1
while i<10:
    print(i)
    i +=1
    #นัชธ์ชาญยุทธ พัชรทับอุไร ม.6/11 เลขที่14