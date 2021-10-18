#지역변수와 전역변수
#지역변수 : 그 지역에서만 부를수 있는 변수(함수 안에 있는 변수)
#전역변수 : 어디서든 부룰수 있는 변수

gun = 10 #전역 변수

def checkpoint(soldiers): #경계근생
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers #지역변수
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #리턴을 해줌으로써 계산된 값이 회부로 나오게 해준다

#함수 내의 gun 변수만 인식하여 오류 발생
print("전체 총 : {0}".format(gun))
#checkpoint(2) #2명이 경계 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))