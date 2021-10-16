from random import *;

x = random.random()
print(x) # 랜덤으로 값을 뽑음

print(int(random())) # 정수값만 랜덤으로 뽑음

print(int(random() * 10)) # 10 미만의 값을 랜덤으로 뽑음

print(int(random() * 10)+1) #1 ~ 10 미만의 값을 랜덤으로 뽑음


# range(1,46) 1부터 46 미만의 값을 가진다.
# range(1,7) = [1, 2, 3, 4, 5, 6]
print(randrange(1,46)) #1 ~ 46 미만의 값 랜덤으로 뽑음
print(randint(1,46)) #1 ~ 46 미만의 값 랜덤으로 뽑음 

a = range(1,7)
print(a)
random.shuffle(a) # 시퀀스를 섞음 하지만 인덱스 고유값은 그대로 유지
random.choice(a) # 랜덤으로 하나의 값 선택

user = [1, 2, 3]
print(sample(user, 1)) #유저에서 1개를 임의로 뽑아서 출력