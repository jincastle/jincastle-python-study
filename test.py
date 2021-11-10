# class Database:
#   def __init__(self, name, size):
#   # 아래에 코드를 작성해 주세요.
#     self.name = name
#     self.size = size
#     name = {}
#     if len(name) > size:
#       return "저장하지마"

#   def insert(self, field, value):
#    # 아래에 코드를 작성해 주세요.
#     self.field = field
#     self.value = value 
#     self.name[field] = value

#   def select(self, field):
#    # 아래에 코드를 작성해 주세요.
#     if self.name[field]  == None:
#       return None
#     else:
#       return self.name[field]
#   def update(self, field, value):
#     if self.name[field]  == None:
#       return None
#     else:
#       return self.name[field] == value

  
#   def delete(self, field):
#     return self.name[field]


# import sys
# print(sys.version)


#문제
# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.
# class Student:
#     def __init__(self, kor, mat, eng):
#         self.__kor = kor
#         self.__mat = mat
#         self.__eng = eng
 
#     @property
#     def kor(self):
#         return self.__kor
 
#     @property
#     def mat(self):
#         return self.__mat
 
#     @property
#     def eng(self):
#         return self.__eng
 
#     def get_total(self):
#         return self.__kor + self.__mat + self.__eng
 
 
# t_str = input()
# t_str = t_str.split(", ")
# t_str = list(map(int, t_str))
# student = Student(t_str[0], t_str[1], t_str[2])
# print("국어, 영어, 수학의 총점: {0}".format(student.get_total()))



# 1.다음과 같은 도시목록의 리스트가 주어졌을때, 도시이름이 S로 시작하지 않는 도시만 리스트로 만들 때 리스트 컴프리헨션을 사용하여 함수를 작성해 보세요.

# cities = ["Tokyo", "Shanghai", "Jakarta", "Seoul", "Guangzhou", "Beijing", "Karachi", "Shenzhen", "Delhi"]

# 2.다음과 같은 도시, 인구수가 튜플의 리스트로 주어졌을때, 키가 도시, 값이 인구수인 딕셔너리를 딕셔너리 컴프리헨션을 사용한 함수를 작성해 보세요.

# population_of_city = [("Tokyo", 36923000), ("Shanghai", 34000000), ("Jakarta", 30000000), ("Seoul", 25514000), ("Guangzhou", 25000000), ("Beijing", 24900000), ("Karachi", 24300000)]


# # cities = ["Tokyo", "Shanghai", "Jakarta", "Seoul", "Guangzhou"]

# # li = [i for i in population_of_city if list(i[0])[0] == "S"]
# # print(li)
# def lllll(list_my):
#   for i in list_my:
#     if list(i[0])[0] == "S":
#       return i[0]

# lllll(population_of_city)


import functools # 데코레이터를 두개 연달아 사용하기 (from functools import warps로도 사용가능)
def is_multiple(x):
    def real_deco(func):
        @functools.wraps(func) # 데코레이터를 두개 연달아 사용할 경우 'wrapper의 반환값은 {1}의 배수입니다.'로 출력되는것을 방지
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            elif r % x != 0:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_deco
@is_multiple(3) # functools.wraps가 데코레이터를 유지시켜줌
@is_multiple(4)
def add(a , b):
    return a + b
print(add(10, 20))