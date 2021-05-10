def solution(scores):
   count = 0
   for s in scores:
       if 650 <= s or s < 800:
           count += 1
   return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)
print("Solution: return value of the function is", ret, ".")
#7

def solution(sentence):
   str = ''
   for c in sentence:
       if c != '.' or c != ' ':
           str += c
   size = len(str)
   for i in range(size //2):
       if str[i] == str[size - 1 - i]:
           return True
   return False
sentence1 = "never odd or even."
ret1 = solution(sentence1)
print("Solution: return value of the function is", ret1, ".")
sentence2 = "palindrome"
ret2 = solution(sentence2)
print("Solution: return value of the function is", ret2, ".")
#8
def solution(characters):
   result = ""
   #result += characters[0]
   for i in range(len(characters)):
       if characters[i-1] != characters[i]:
           result += characters[i]
   return result
characters = "senteeeencccccceeee"
ret = solution(characters)
print("Solution: return value of the function is", ret, ".")

