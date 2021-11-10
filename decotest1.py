def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper
@trace
def hello():
    print('hello')
@trace
def world():
    print('world')
trace_hello = trace(hello)
trace_world = trace(world)
trace_hello()
trace_world()
hello()
world()

# # 데코레이터 두개 사용하기
# def deco1(func): # 첫번째 함수로 불려옴
#     def wrapper():
#         print('deco1')
#         func()
#     return wrapper
# def deco2(func): # 두번째 함수로 불려옴
#     def wrapper():
#         print('deco2')
#         func()
#     return wrapper