# 반복문


#print("대기번호 : 1")
#print("대기번호 : 2")
#print("대기번호 : 3")
#print("대기번호 : 4")

#for문

# for waiting_no in [1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1,5):
#     print("대기번호 : {0}".format(waiting_no))

#응용
#출석번호가 1 2 3 4, 앞에 100dmf 붙이기로 함 ->100, 101, 102, 103

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "black widow"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "black widow"]
students = [i.upper() for i in students]
print(students)

# -------------------------------------

#continue break
#결석 처리
# absent = [2, 5] #결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1,11):
#     if student in absent:
#         continue #조건에 맞으면 스킵하고 다시 반복
#     elif student in no_book:
#         print("수업 여기까지. {0}는 굠실로 따라와".format(student))
#         break #조건에 맞으면 반복문 종료
#     print("{0}, 책을 읽어봐".format(student))

# -------------------------------------

#while 문

#커피 주문 대기순위

# hero = "아이언맨"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다.{1} 번 대기해 주세요".format(hero, index))
#     index -= 1
#     if index == 0:
#         print("남은 주문이 없습니다.")

# -------------------------------------
# customer = "블랙위도우"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? "위