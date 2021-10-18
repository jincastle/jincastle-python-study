#pickle 모듈
#일반 텍스트를 파일로 저장할 때는 파일 입출력을 이용

import pickle
# profile_file = open("profile.pickle", "wb") #b는 바이러 타입 pickle을 사용할려면 넣어야 한다
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를 file에 저장
# profile_file.close


# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

#with
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file)요

#pickle 없이 파일 불러오기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())