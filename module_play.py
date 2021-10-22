# import module
# module.price(3)
# module.price_morning(4)

# import module as mv # module에 mv이라는 별명을 붙여서 사용
# mv.price(3)
# mv.price_morning(4)

# from module import * # 모두 호출
# price(3)
# price_morning(4)

# from module import price, price_morning # 필요한것만 호출
# price(5)
# price_morning(4)

from module import price_soldier as price # 필요한걸 호출하고 별명을 준다
price(5) #군인 가격