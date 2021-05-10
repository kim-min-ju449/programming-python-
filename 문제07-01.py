a="neven"
a ="seven"

if (a[0] ==a[4]) and (a[1] ==a[3]):
    print('팰린드롬이다')

if a[0] != a[4]:
    print("팰린드롬이 아니다")
elif a[1] !=a[3]:
    print("팰린드롬이 아니다")
else:
    print("팰린드롬이 아니다.")

#i값 0,1
for i in range(2):
    if a[i]!=a[4-i]:
        print("팰린드롬이 아니다")

a="enevene"
if a[0] != a[6]:
    print("팰린드롬이 아니다")
elif a[1] !=a[5]:
    print("팰린드롬이 아니다")
elif a[2] !=a[4]:
    print("팰린드롬이 아니다")
else:
    print("팰린드롬이 아니다.")

for i in range(3):
    if a[i] != a[6-i]:
        print("팰린드롬이 아니다")
    else:
        print("팰린드롬이다.")