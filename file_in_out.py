# score_file = open("score.txt", "w", encoding="utf8") #open 파일을 열고 w는 write 쓰기 utf8형식으로 불러오기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #a =uphand 업어 쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

#파일 읽어오기
# score_file = open("score.txt", "r", encoding="utf8") #r = reading
# print(score_file.read()) #전체 읽어오기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #r = reading
# print(score_file.readline()) #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") #줄바꿈이 싫을때 end를 넣어준다
# print(score_file.readline(), end="") 
# print(score_file.readline())
# score_file.close()

#파일에 몇줄인지 모를 때 
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

