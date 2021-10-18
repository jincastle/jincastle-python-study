#class : 틀
#스타크래프트로 설명

#__init__ : 객체를 생성할때 , self를 제외한 매개변수 값을 다줘야 실

#클래스 사용 유닛 생성
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name #멤버 변수로 초기화
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#레이스 : 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) #레이스에 대한 멤버 변수 호출

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것( 빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking() == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#클래스 없이 유닛 생성
# #마린
# name = "마린" 
# hp = 40 #체력
# damage = 5 #공격력

# print("{0} 유닛이 생성되었습니다".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# #탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)


