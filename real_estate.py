class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("--------------------------------")
        print("location : {}\nhouse_type : {}\ndeal_type : {}\nprice : {}\ncompletion_year : {}"\
        .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


houses = []

trapellis = House("gangnam", "Apart", "매매", "10억", "2010년")

mapo_hi = House("mapo", "office_tel", "전세", "5억", "2007년")

songpasbil = House("songpa", "billa", "월세", "500/50", "2000년")

houses.extend([trapellis,mapo_hi,songpasbil])

print("총 {}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()