#가변인자를 이용한 함수 호출
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name,age), end="") #end를 넣어줌으로써 줄바꿈 없이 연결되서 출력
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("하하", 20, "python", "java", "c", "c++", "c#") 
# profile("유재석", 25, "python", "java", "", "", "") #값이 없는 경우 빈공간


def profile(name, age, *language):
     print("이름 : {0}\t 나이 : {1}\t".format(name,age), end=" ") 
     for lang in language:
         print(lang, end=" ")
     print()

profile("하하", 20, "python", "java", "c", "c++", "c#") 
profile("유재석", 25, "python", "java") 