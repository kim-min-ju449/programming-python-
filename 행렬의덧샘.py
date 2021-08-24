def solution(arr1, arr2):
    answer = [0] *2
    answer = [answer]*2
    answer[0][0] = arr1[0][0]+arr2[0][0]
    return answer[0][0]

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]