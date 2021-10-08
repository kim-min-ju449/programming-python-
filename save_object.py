#python 객체 그대로 저장하자
import pickle
class Person:
    def __init__(self,name, music):
            self.name=name
            self.age=music

    def _str__(self):
            return f'이름:{self.name}\t좋아하는 음악:{self.music}'

번호1 = Person('공도윤','곰세마리')
번호4 = Person('김설','stay')
절친 = [번호1, 번호4]
with open('object.bin','wb') as f:
    pickle.dump(번호1, f)
with open('objects.bin','wb') as f:
    pickle.dump(절친, f)