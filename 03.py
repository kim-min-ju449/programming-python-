def 보조함수_a(arr):
   counter = [0]*1001
   for x in arr:
       counter[x] += 1
   return counter

def 보조함수_b(arr):
   ret = 0
   for x in arr:
       if ret < x:
           ret = x
   return ret

def 보조함수_c(arr):
   INF = 1001
   ret = INF
   for x in arr:
       if x != 0 and ret > x:
           ret = x
   return ret

def solution(arr):
   counter = 보조함수_a(arr)
   max_cnt = 보조함수_b(counter)
   min_cnt = 보조함수_c(counter)
   return max_cnt // min_cnt

#The following is code to output testcase.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
