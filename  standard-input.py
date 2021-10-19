#표준 입출력
# print("Python", "Java", sep=",", end="?") #sep는 문자간의 사이에 띄어쓰기 대신 넣는걸 결정하고
# print("무엇이 더 재밌을까요?") #end로 인해 위 문장과 연결해서 나옴

# import sys
# print("Python", "Java", file=sys.stdout)  # 표준 출력
# print("Python", "Java", file=sys.stderr)  # 표준 에러시 따로 로깅됨

# 시험 성적
# scores ={"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust(8) 왼쪽에 8칸의 공간을 두고 왼쪽 정렬, #rjust(4) 오른쪽 4 공간을 두고 오른쪽 정렬

# 수학      :   0
# 영어      :  50
# 코딩      : 100

#은행 대기 순번표
# 001, 002 앞에 00붙게 ..
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) #zfill(크기) 3공간에 값이 없는 공간에 0을 넣는다 

# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# .
# .

#사용자 입력값은 무조건 str 로 인식된다
# answer = input("아무 값이나 입력하세요 : ") 
# print("입력하신 값은 "+ answer + "입니다.")