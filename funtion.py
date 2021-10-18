# 함수 정의 def

#계좌생성
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

#입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money

#출금
def withddraw(balance, moeny):
    if balance >= moeny:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - moeny))
        return balance - moeny
    else:
        print("잔액이 부족합니다.")

#저녁 출금
def withddraw_night(balance, money):
    commission = 1000
    return commission, balance - money - commission


balance = 10000
balance = deposit(balance, 1000)
#balance = withddraw(balance, 5000)
#balance = withddraw(balance, 50000)
commission, balance = withddraw_night(balance, 1000)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))



#기본값 키워드 호출
def profile(name, age = 17, main_lang = "파이썬"): #기본값 설정
    print("이름 : {0} 나이 : {1} 사용 언어 {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬") # 값 설력
profile("김태호") #값설정 없을시 기본값
profile(name="유재석", main_lang="java", age=20) #키워드 호출

