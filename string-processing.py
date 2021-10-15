#문자열 처리 함수

python = "Python is Amazing"

print(python.lower()) # 모든 문자를 소문자로 변환

print(python.upper()) # 모든 문자를 대문자로 변환

print(python[0].isupper()) #해당 위치에 있는 문자가 대문자면 true 아니면 false

print(len(python)) #문자 길이를 알려주는 함수 17

print(python.replace("Python", "Jave")) # 해당 문자를 찾아 변환 Python -> Java (변수.replace("찾는 문자", "변화할 문자"))

index = python.index("n") #해당 문자가 나오는 첫번째 인덱스를 찾음
print(index) # 5
index = python.index("n", index+1) #2번째 n이 나오는 인덱스를 찾음 index+1은 index는 출발지점 첫번째 n인 5부터 출발 그 뒤에 n을 찾는다
print(index) # 15

print(python.find("n")) #해당 문자를 찾는 함수 5 
print(python.find("Java")) #만약 없는 문자를 찾으면 -1 이 나옴 인데스로 없는 문자를 찾으면 에러

print(python.count("n")) # 해당 문자 개수를 알려줌