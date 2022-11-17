
a=[]
while True:
    b=input("enter your id: ")
    a.append(b)
    if b=="end":
        break
a.remove("end")

for i in a:
    c=i.split("@")
    print(c)
    # print("For",i)  #this line is use to understanding
    print()
print(">>>>>>> DOMAIN: ",c[1])
print(">>>>>>> USER NAME: ",c[0])



