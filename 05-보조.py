#1 부터 해당하는 숫자까지 박수를 총 몇 번 쳐야 하는가?

a = 13

counter =0

for num in range(1, a+1):
    #해당하는 숫자가 박수를 몇번 치는지
    문자열=str(a)
    while num:
        if num%10==3 or num%10==6 or num%10==9:
            counter +=1
        num = num//10
print(counter)