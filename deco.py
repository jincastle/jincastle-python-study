# @로 시작하는 메서드 : 데코레이터
#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
# 데코레이터 두개 사용하기
def deco1(func): # 첫번째 함수로 불려옴
    def wrapper():
        print('deco1')
        func()
    return wrapper
def deco2(func): # 두번째 함수로 불려옴
    def wrapper():
        print('deco2')
        func()
    return wrapper
@deco1
@deco2
def hello_world(): # 세번째 함수로 불려옴
    print('hello world!')
hello_world()
# 변수를 받는 데코레이터
def deco3(func):
    def wrapper(a, b):
        r = func(a, b)
        print('{0}(a = {1}, b = {2} -> {3})'.format(func.__name__, a, b, r))
        return r
    return wrapper
@deco3
def add(a, b):
    return a + b
print(add(1, 3))
# 변수가 있는 데코레이터 만들기
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
# class 데코레이터 사용
class Trace:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 끝')
@Trace
def hello():
    print('hello')
hello()
# 클래스로 매개변수와 반환값처리
class Trace:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs): # 클래스를 호출했을 때 동작하는 메서드
        r = self.func(*args, **kwargs)
        print('{0}(args = {1}, kwargs = {2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r
@Trace
def add(a, b):
    return a + b
add(10, 20)
add(a = 10, b = 20)
# 매개변수를 받는 클래스 데코레이터
class Ismultiple:
    def __init__(self, x):
        self.x = x
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            elif r % self.x != 0:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper
@Ismultiple(3)
def add(a, b):
    return a + b
print(add(30, 30))
print(add(30, 20))
# 연습문제1
class type_check:
    def __init__(self, type_a, type_b):
        self.type_a = type_a
        self.type_b = type_b
    def __call__(self,func):
        def wrapper(a, b):
            if isinstance(a, self.type_a) and isinstance(b, self.type_b):
                r = func(a, b)
                return r
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
@type_check(int, int)
def add(a, b):
    return a + b
print(add(10, 20))
# 연습문제2
def html_tag(x):
    def decofunc(func):
        def wrapper():
            return '<{0}>{1}</{0}>'.format(x, func())
        return wrapper
    return decofunc
a, b = input().split()
@html_tag(a)
@html_tag(b)
def helo():
    return 'Hello, world!'
print(helo())# @로 시작하는 메서드 : 데코레이터
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
# 데코레이터 두개 사용하기
def deco1(func): # 첫번째 함수로 불려옴
    def wrapper():
        print('deco1')
        func()
    return wrapper
def deco2(func): # 두번째 함수로 불려옴
    def wrapper():
        print('deco2')
        func()
    return wrapper
@deco1
@deco2
def hello_world(): # 세번째 함수로 불려옴
    print('hello world!')
hello_world()
# 변수를 받는 데코레이터
def deco3(func):
    def wrapper(a, b):
        r = func(a, b)
        print('{0}(a = {1}, b = {2} -> {3})'.format(func.__name__, a, b, r))
        return r
    return wrapper
@deco3
def add(a, b):
    return a + b
print(add(1, 3))
# 변수가 있는 데코레이터 만들기
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
# class 데코레이터 사용
class Trace:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 끝')
@Trace
def hello():
    print('hello')
hello()
# 클래스로 매개변수와 반환값처리
class Trace:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs): # 클래스를 호출했을 때 동작하는 메서드
        r = self.func(*args, **kwargs)
        print('{0}(args = {1}, kwargs = {2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r
@Trace
def add(a, b):
    return a + b
add(10, 20)
add(a = 10, b = 20)
# 매개변수를 받는 클래스 데코레이터
class Ismultiple:
    def __init__(self, x):
        self.x = x
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            elif r % self.x != 0:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper
@Ismultiple(3)
def add(a, b):
    return a + b
print(add(30, 30))
print(add(30, 20))
# 연습문제1
class type_check:
    def __init__(self, type_a, type_b):
        self.type_a = type_a
        self.type_b = type_b
    def __call__(self,func):
        def wrapper(a, b):
            if isinstance(a, self.type_a) and isinstance(b, self.type_b):
                r = func(a, b)
                return r
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
@type_check(int, int)
def add(a, b):
    return a + b
print(add(10, 20))
# 연습문제2
def html_tag(x):
    def decofunc(func):
        def wrapper():
            return '<{0}>{1}</{0}>'.format(x, func())
        return wrapper
    return decofunc
a, b = input().split()
@html_tag(a)
@html_tag(b)
def helo():
    return 'Hello, world!'
print(helo())