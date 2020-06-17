#import theater_module as tm

#tm.price(3) #3명 영화표 가격
#tm.price_morning(4) #4명 조조 할인 가격
#tm.price_soldier(5) #5명 군인 할인 가격
 

#from theater_module import *
#price(3)
#price_morning(4)
#price_soldier(5)

from theater_module import price, price_morning
try:
    price(5)
    price_morning(6)
    price_soldier(6)
except NameError:
    print("함수가 없습니다.")