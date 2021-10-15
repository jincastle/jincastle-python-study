#list
#subway = []

subway = [10 , 20 , 30]
print(subway)

subway = ["유재석", "하하", "박명수"]
print(subway)

# 하하는 몇 번째 칸에 있는가?(위치 찾기)
print(subway.index("하하"))

# 노홍철이 다음 칸에 탐(추가)
subway.append("노홍철")
print(subway)
subway.add("정준하")

#정형돈을 유재석 하하 사이에 추가(중간에 추가)
subway.insert(1, "정형돈")
print(subway)

# 한명씨 내린다.#맨뒤에있는 사람 제외
print(subway.pop()) 
print(subway)

#중복값 개수 찾기
subway.append("유재석")
print(subway)
print(subway.count("유재석")) #유재석 이 몇명 있나개수 확인

#정렬 기능
num_list = [5, 4, 1, 2, 3]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
#num_list.clear()
#print(num_list)

# 다양한 자료형 함께 사용
mix_list = [1, "유재석", True]

# list 확장 합치기
num_list.extend(mix_list)
print(num_list)