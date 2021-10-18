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

#다양한 format 출력

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: > 10}".format(500))
#양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
print("{0:+,}".format(-10000000000))
#3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
#돈이 많으면 행복하니까 빈 자리는  ^ 로 채워주기
print("{0:^<+30,}".format(10000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점을 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))
