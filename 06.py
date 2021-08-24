def solution(scores):
   count = 0
   for s in scores:
       if 650 <= s and s < 800:
           count += 1
   return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

def solution(number):
   count = 0
   for i in range(1, number + 1):  # for(int i=1; i<number+1)
       current = i
       temp = count
       while current != 0:
           if current%10%3 ==0 and current%10 !=0:
               count += 1
               print("pair", end = '') # 디버깅을 위한 출력(없어도 무관)
           current = current // 10
       if temp == count:
           print(i, end = '') # 디버깅을 위한 출력(없어도 무관)
       print(" ", end = '') # 디버깅을 위한 출력(없어도 무관)
   print("") # 디버깅을 위한 출력(없어도 무관)
   return count
