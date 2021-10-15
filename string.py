#기본 문자열
string = '나는 man입니다.'
print(string)
string2 = "나는 girl입니다"
print(string2)
string3 = """
나는 man입니다,
나는 girl입니다.
"""
print(string3)


#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])

print("연 : " + jumin[0:2]) # 0부터 2전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 뒤에서 부터 7번째 시작으로 끝까지 

#format print에 정수 문자 문자열 넣기

#방법1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." %"파이썬")
print("Apple 은 %c로 시작해요" %"A")
#%s
print("나는 %s살입니다." %20)
print("나는 %s살입니다." %20)#print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법2
#format
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) 

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {color}살이며, {age}색을 좋아해요.".format(age=20, color="빨간"))

#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")