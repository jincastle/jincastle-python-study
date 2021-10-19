#dictionary 구분 key와 value로 구성

#from typing import Concatenate


cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3]) # 키값을 부르면 value 값을 출력 :유재석
print(cabinet[100]) # :김태호
print(cabinet.get(3)) # 유재석

# 키값이 사용중인지 아닌지 확인
print(cabinet.get(5)) #:none
print(cabinet.get(5, "사용 가능")) #: 사용가능

#해당 dictionary안에 키값이 있는지 없는지 확인
print(3 in cabinet) #:True
print(5 in cabinet) #:False

# 변경 및 새로 추가
print(cabinet)
cabinet[3] = "전소민" # 유재석 -> 전소민으로 바낌
cabinet[4] = "송지효" # 송지효 추가
print(cabinet)

# 삭제
del cabinet[3]
print(cabinet)

#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key value 둘다 출력
print(cabinet.items())

# 모두 삭제
cabinet.clear()