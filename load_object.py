import pickle
from save_object import Person

with open('object.bin','rb')as f:
    data=pickle.load(f)
print(f'load한 데이터:'+{data})

#객체 하나 가져오자
with open('objects.bin','rb')as f:
    data = pickle.load(f)
print(data)

#리스트 객체 가져오자
with open('objects.bin','rb')as f:
    data = pickle.load(f)
for d in data:
    print(d)